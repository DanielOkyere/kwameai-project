// import Sidebar from "../components/Sidebar";
import Feed from "../components/FeedLayout";
// import Rightbar from "../components/Rightbar";
import { Box, 
  createTheme, 
  // Stack, 
  ThemeProvider } from "@mui/material";
// import Navbar from "../components/Navbar";
// import Add from "../components/Add";
import { useState } from "react";

function FeedPage(props: any) {
  const [mode, setMode] = useState("light");

  const darkTheme = createTheme({
    palette: {
      mode: mode,
    },
  });
  return (
    <ThemeProvider theme={darkTheme}>
      <Box bgcolor={"background.default"} color={"text.primary"}>
        {/* <Navbar /> */}
          <Feed />
        {/* <Stack direction="row" spacing={2} justifyContent="space-between"> */}
        {/* <Sidebar setMode={setMode} mode={mode}/> */}
          {/* <Rightbar /> */}
        {/* </Stack> */}
        {/* <Add /> */}
      </Box>
    </ThemeProvider>
  );
}

export default FeedPage;
