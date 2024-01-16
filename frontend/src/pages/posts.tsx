import {
  Create,
  Datagrid,
  Edit,
  EditButton,
  List,
  SimpleForm,
  TextField,
  TextInput,
  BooleanInput
} from "react-admin";
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CardActions from '@mui/material/CardActions';
import Button from '@mui/material/Button';


export const PostList = (props: any) => (
    <List {...props} filters={[]}>
    <Datagrid rowClick="edit">
        <Card >
            <CardMedia sx={{height: 150}} image="https://picsum.photos/1200/1200"/>
             <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                <TextField source="title"/>
                </Typography>
                <Typography variant="body2" component="div">
                <TextField source="content"/>
                </Typography>
            </CardContent>
            <CardActions>
            <Button size="small">
            <TextField source="published"/>

            </Button>
            </CardActions>
        </Card>
    </Datagrid>
    </List>
);

export const PostEdit = (props: any) => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput source="title"/>
            <TextInput source="content"/>
        </SimpleForm>
    </Edit>
);


export const PostCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="title" />
      <TextInput source="content" />
        <TextInput source="published" />
    </SimpleForm>
  </Create>
);

