import { createBrowserHistory as createHistory } from "history";
import simpleRestProvider from "ra-data-simple-rest";
import { Admin, fetchUtils, Resource, CustomRoutes } from "react-admin";
import { Route } from "react-router";
import MyLayout from "./components/AdminLayout";
// import Dashboard from "./pages/Dashboard";
import { PostCreate, PostEdit, PostList } from "./pages/posts"
import LoginPage from "./pages/Login";
import { ProfileEdit } from "./pages/ProfileEdit";
import Register from "./pages/Register";
import { UserEdit, UserList } from "./pages/Users";
import authProvider from "./providers/authProvider";
import { basePath } from "./providers/env";
import PostIcon from "@mui/icons-material/PostAdd";
import PersonIcon from "@mui/icons-material/Person";
import FeedIcon from "@mui/icons-material/Feed"
import FeedPage from "./pages/FeedPage";

const httpClient = (url: string, options: any = {}) => {
  options.user = {
    authenticated: true,
    token: `Bearer ${localStorage.getItem("token")}`,
  };
  if (url.includes("/users/") && options.method === "PUT") {
    // We use PATCH for update on the backend for users, since PATCH is selective PUT, this change should be fine
    options.method = "PATCH";
  }
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider(`${basePath}/api/v1`, httpClient);

const App = () => {
  return (
    <Admin
      disableTelemetry
      dataProvider={dataProvider}
      authProvider={authProvider}
      loginPage={LoginPage}
      history={createHistory()}
      layout={MyLayout}
    >
      <CustomRoutes>
        <Route path="/my-profile" element={<ProfileEdit />} />
      </CustomRoutes>
  
  
      <CustomRoutes noLayout>
        <Route path="/register" element={<Register />} />
      </CustomRoutes>
      {(permissions) => [
        permissions.is_superuser === true ? (
          <Resource
            options={{ label: "Users" }}
            name="users"
            list={UserList}
            edit={UserEdit}
            icon={PersonIcon}
          />
        ) : null,
        <Resource
          name="feeds"
          options={{ label: "Feeds" }}
          list={FeedPage}
          icon={FeedIcon}
        />,
        <Resource
          name="posts"
          options={{ label: "Posts" }}
          list={PostList}
          edit={PostEdit}
          create={PostCreate}
          icon={PostIcon}
        />,
      ]}
    </Admin>
  );
};

export default App;
