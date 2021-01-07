import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import config from "./config";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import search from "./search";
import TagItems from "./TagItems"

function Resources() {
  const [data, setData] = useState([]);
  const [searchTerms, setSearchTerms] = useState("");
  const handleChange = (event) => {
    setSearchTerms(event.target.value);
  };

  useEffect(() => {
    async function getData() {
      const result = await axios(
        `https://${config.endpoint}/api/v2/public/resources`
      );
      let data = [];
      for (let item of result.data) {
        let terms = [];
        let tags = [];
        if ("erp_bai_1_name" in item && item.erp_bai_1_name != null) {
          terms.push(item.erp_bai_1_name.toLowerCase());
        }
        if ("erp_cli_8_tags" in item && item.erp_cli_8_tags != null) {
          tags = item.erp_cli_8_tags.split(",").map((item) => item.trim());
          terms = terms.concat(tags);
        }
        item["terms"] = terms;
        item["tags"] = tags;
        data.push(item);
      }

      setData(data);
    }

    getData();
  }, []);

  let filtered = [];
  if (data) {
    filtered = search(data, searchTerms);
  }

  let resources = [];
  for (let item of filtered) {
    let imgURL = null;
    if (item.erp_mri_3_logo !== null) {
      imgURL = item.erp_mri_3_logo;
    }
    resources.push(
      <ResourceItem
        key={item.id}
        id={item.id}
        title={item.erp_bai_1_name}
        img={imgURL}
        abbr={item.erp_bai_1_name}
        web={item.erp_bai_4_webpage}
        desc={item.erp_mri_2_tagline}
        providers={item.erp_bai_3_providers_public}
        tags={item.tags}
      />
    );
  }

  return (
    <div className="container-fluid">
      <div className="mt-5">
        
        
        <h2 style={{color:config.colorA}} className="text-center title"><FontAwesomeIcon icon="database" style={{ color: config.colorA }} /> Resources</h2>

        <input
          className="form-control m-2 p-4 rounded col-6 mx-auto"
          type="text"
          placeholder="Search"
          value={searchTerms}
          onChange={handleChange}
        />
        <br />
      </div>

      <div className="row">{resources}</div>
    </div>
  );
}

function ResourceItem(props) {


  let logo = null;
  if (props.img) {
    logo = <img className="mw-75 logo" src={props.img} alt="service logo" />;
  } else {
    logo = <FontAwesomeIcon icon="cloud" size="5x" style={{ color: "grey" }} />;
  }

  let desc = null;
  if (props.desc) {
    desc = <div className="quote">{props.desc}</div>;
  }

  return (
    <div className="col-lg-3 col-md-6 col-sm-12 mb-4">
      <div className="card text-center h-100 plick">
        <div className="card-image">
          <div className="placeholder">{logo}</div>
        </div>

        <div className="card-body d-flex flex-column">
          <h6>
            <strong>
              <Link className="title" to={"/resources/" + props.id} style={{color:config.colorA}}>
                {props.title}
              </Link>
            </strong>
          </h6>
          {desc}


          
          <div className="mt-auto">
            <Link
              className="btn btn-dark btn-outline"
              to={"/resources/" + props.id}
            >
              View Service
            </Link>
            { (props.tags.length > 0) && <hr/>}
            <TagItems  items={props.tags} simple></TagItems>
          </div>
         
            
          

          {/* {website} */}

          {/* <ProviderItems className="mt-auto" items={props.providers} />
          <TagItems className="mt-auto" items={props.tags} /> */}
        </div>
      </div>
    </div>
  );
}


export default Resources;
