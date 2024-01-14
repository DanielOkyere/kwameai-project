from typing import Any, List, Optional

from fastapi import APIRouter, HTTPException
from sqlalchemy import func, select
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.deps.request_params import PostRequestParams
from app.deps.users import CurrentUser
from app.models.posts import Posts
from app.schemas.posts import Post as PostSchema
from app.schemas.posts import Postcreate, Postupdate

router = APIRouter(prefix="/posts")


@router.get("", response_model=List[PostSchema])
async def get_posts(
    response: Response,
    session: CurrentAsyncSession,
    request_params: PostRequestParams,
    user: CurrentUser,
) -> Any:
    total = await session.scalar(
        select(func.count(Posts.id).filter(Posts.user_id == user.id))
    )
    items = (
        (
            await session.execute(
                select(Posts)
                .offset(request_params.skip)
                .limit(request_params.limit)
                .order_by(request_params.order_by)
                .filter(Posts.user_id == user.id)
            )
        )
        .scalars()
        .all()
    )
    response.headers[
        "Content-Range"
    ] = f"{request_params.skip}-{request_params.skip + len(items)}/{total}"
    return items


@router.post("", response_model=PostSchema, status_code=201)
async def create_post(
    post_in: Postcreate,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    post = Posts(**post_in.dict())
    post.user_id = user.id
    session.add(post)
    await session.commit()
    return post


@router.put("/{post_id}", response_model=PostSchema)
async def update_post(
    post_id: int,
    post_in: Postupdate,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    post: Optional[Posts] = await session.get(Posts, post_id)
    if not post or post.user_id != user.id:
        raise HTTPException(404)
    update_data = post_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(post, field, value)
    session.add(post)
    await session.commit()
    return post


@router.get("/{post_id}", response_model=PostSchema)
async def get_post(
    post_id: int,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    post: Optional[Posts] = await session.get(Posts, post_id)
    if not post or post.user_id != user.id:
        raise HTTPException(404)
    return post


@router.delete("/{post_id}")
async def delete_post(
    post_id: int,
    session: CurrentAsyncSession,
    user: CurrentUser,
) -> Any:
    post: Optional[Posts] = await session.get(Posts, post_id)
    if not post or post.user_id != user.id:
        raise HTTPException(404)
    await session.delete(post)
    await session.commit()
    return {"success": True}
