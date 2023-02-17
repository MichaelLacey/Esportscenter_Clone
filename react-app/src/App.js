import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <BrowserRouter>
      <Navigation isLoaded={isLoaded} />
      
        <Switch>
          {/* <Route path="/login" > <LoginFormPage /> </Route>
          <Route path="/signup"> <SignupFormPage /> </Route> */}


        </Switch>
      
    </BrowserRouter>
  );
}

export default App;
