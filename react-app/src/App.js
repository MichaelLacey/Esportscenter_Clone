// import React, { useState, useEffect } from "react";
// import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import Homepage from "./components/HomePage";
import Navigation from "./components/Navigation";
import GamePage from "./components/GamePage";

function App() {
  // const dispatch = useDispatch();


  return (

    <>
      <Navigation />
      <Switch>
        <Route path='/' exact={true}> <Homepage /></Route>
        <Route path='/:gameName/:gameId' > <GamePage /></Route>


      </Switch>

    </>

  );
}

export default App;
