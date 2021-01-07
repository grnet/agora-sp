import "./App.css";
import { React } from "react";
import Providers from "./Providers";
import Provider from "./Provider";
import Resources from "./Resources";
import Resource from "./Resource";
import config from "./config"


import Navigation from "./Navigation";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faGlobeAmericas,
  faCloud,
  faTag,
  faPhotoVideo,
  faBook,
  faAtom,
  faCogs,
  faEnvelope,
  faPhone,
  faLock,
  faUser,
  faPenFancy,
  faArchive,
  faDatabase,
  faTrophy,
  faProjectDiagram,
  faCoins,
  faClipboard,
  faMapMarker,
  faBalanceScale,
  faFlask,
  faMicroscope,
  faMapMarkedAlt,
  faInfoCircle,
  faUniversity,
} from "@fortawesome/free-solid-svg-icons";

library.add(
  faGlobeAmericas,
  faCloud,
  faTag,
  faPhotoVideo,
  faBook,
  faAtom,
  faCogs,
  faEnvelope,
  faPhone,
  faLock,
  faUser,
  faPenFancy,
  faArchive,
  faDatabase,
  faTrophy,
  faProjectDiagram,
  faCoins,
  faClipboard,
  faMapMarker,
  faBalanceScale,
  faFlask,
  faMicroscope,
  faMapMarkedAlt,
  faInfoCircle,
  faUniversity,

);

function App() {


  let basePath = null;
  if ("basePath" in config) {
    basePath = config.basePath
  }


  return (
    <Router basename={basePath}>
      <div className="App">
        
        <Navigation />
        <Switch>
          <Route path="/providers/:id">
            <Provider />
          </Route>
          <Route path="/resources/:id">
            <Resource />
          </Route>
          <Route path="/providers">
            <Providers />
          </Route>
          <Route path="/">
            <Resources />
          </Route>
         
        </Switch>
      </div>
    </Router>
  );
}

export default App;
