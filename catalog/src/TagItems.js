import React from "react";
import config from "./config";


function TagItems(props) {
    let list = [];
  
    
  
    let badgeClass = "badge text-wrap mr-2 p-2 mb-2"
    let badgeColor = config.colorA
    let badgeStyle =  { "backgroundColor": badgeColor, "color":"white"};
    if (props.color) badgeColor = props.color 
  
    if (props.outline) {
      badgeStyle["backgroundColor"] = "transparency"
      badgeStyle["color"] = badgeColor;
      badgeStyle["border"] = "1px " + badgeColor + " solid";
    } else {
      badgeStyle["backgroundColor"] = badgeColor;
    }
  
  
    if (props.outline) badgeClass = badgeClass + " outline"
  
    if (!props.items || (props.items && props.items.length === 0)) return null;
    for (let item of props.items) {
      if (item === undefined) continue;
      if (props.simple) {
        list.push(
          <span key={item} className={badgeClass} style={badgeStyle} >
            {item}
          </span>
        );
      } else {
        list.push(
          <span key={item.id} className={badgeClass} style={badgeStyle}>
            {item[props.valueOfKey]}
          </span>
        );
      }
    }
  
    let result = null;
  
    if (props.label) {
      result = <span className="mr-2">{props.label}: </span>;
    }
  
    return (
      <div>
        {result}
        {props.breakpoint && <br />}
        {list}
      </div>
    );
  }
  
  export default TagItems;