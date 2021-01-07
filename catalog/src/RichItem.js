import React from "react";

function RichItem(props) {
    if (!props.item) return null;
  
    let border = "";
    if (props.border) border = "quote-border";
  
    return (
      <div>
        {props.label && <span className="mr-2">{props.label}:</span>}
        <div
          className={border + " p-3"}
          dangerouslySetInnerHTML={{
            __html: props.item,
          }}
        />
      </div>
    );
  }

  export default RichItem;