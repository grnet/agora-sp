import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

function ValueItem(props) {
    if (!props.item) return null;
  
    let icon = null;
    if (props.icon) {
      icon = <FontAwesomeIcon className="mr-2" icon={props.icon} />;
    }
  
    let labelResult = null;
    if (props.label) {
      labelResult = props.label + ": ";
    }
  
    let display = "d-block";
  
    if (props.inline) {
      display = "d-inline-block mr-4";
    }
  
    let stylize = "";
  
    if (props.em) stylize = stylize + " text-emphasis";
    if (props.strong) stylize = stylize + " text-strong";
  
    let pItem = null 
    if (props.valueOfKey){
      pItem = props.item[props.valueOfKey]
    } else {
      pItem = props.item
    }
  
    if (props.link) {
      if (props.url) {
        return (
          <div className={display}>
            <span>{icon}</span>
            {labelResult}
            {props.breakpoint && <br />}
            <a className="grey" href={pItem} target="_blank" rel="noreferrer noopener">
              <span className={stylize}>{props.url}</span>
            </a>
          </div>
        );
      }
      return (
        <div className={display}>
          <span>{icon}</span>
          {props.breakpoint && <br />}
          <a className="grey" href={pItem} target="_blank" rel="noreferrer noopener">
            <span className={stylize}>{props.label}</span>
          </a>
        </div>
      );
    }
    return (
      <div className={display}>
        {(icon || labelResult) && (
          <span className="mr-2">
            {icon}
            {labelResult}
          </span>
        )}
        {props.breakpoint && <br />}
        <span className={stylize}>{pItem}</span>
      </div>
    );
  }

  export default ValueItem;