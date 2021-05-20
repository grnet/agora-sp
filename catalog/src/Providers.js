import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import config from "./config";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import search from "./search";
import TagItems from "./TagItems";

const getProvidersOfResources = (resources, orgUUid) => {
  let providers = [orgUUid]
  for (let resource of resources ) {
    if (!!resource.erp_bai_3_providers_public){
      for( let provider of resource.erp_bai_3_providers_public){
        if (providers.indexOf(provider.href)<0){
          providers.push(provider.href)
        }
      }
    }
  }
  return providers;
}

const checkProvider = ( providerUUID, providersUUIDS ) => {
  for( let prov of providersUUIDS ) {
    if (prov.includes(providerUUID)){
      return true;
    }
  }
  return false;
}


function Providers() {
  const [data, setData] = useState([]);
  const [searchTerms, setSearchTerms] = useState("");
  const [showProviders, setShowProviders] = useState([]);
  const [providersGroup, setProvidersGroup] = useState([]);
  const [resourcesGroup, setResourcesGroup] = useState([]);
  const handleChange = (event) => {
    setSearchTerms(event.target.value);
  };

  // Get Providers
  useEffect(() => {
    async function getProviders() {
      const result = await axios(
        `https://${config.endpoint}/api/v2/public/providers/`
      );
      let data = [];
      for (let item of result.data) {
        let terms = [];
        let tags = [];
        if ("epp_bai_1_name" in item && item.epp_bai_1_name != null) {
          terms.push(item.epp_bai_1_name.toLowerCase());
        }
        if ("epp_bai_2_abbreviation" in item && item.epp_bai_2_abbreviation != null) {
          terms.push(item.epp_bai_2_abbreviation.toLowerCase());
        }
        if ("epp_cli_3_tags" in item && item.epp_cli_3_tags != null) {
          tags = item.epp_cli_3_tags.split(",").map((item) => item.trim());
          terms = terms.concat(tags);
        }
        item["terms"] = terms;
        item["tags"] = tags;
        data.push(item);
      }

      setProvidersGroup(data);
    }

    getProviders();
  }, []);

  // Get resources if organisationURL is specified
  useEffect(() => {
    async function getResources() {
      const result = await axios(
        `https://${config.endpoint}/api/v2/public/resources/`
      );
      let data = [];
      for (let item of result.data) {
        let terms = [];
        let tags = [];
        if (!!config.organisationURL &&
          item.erp_bai_2_organisation_public !== config.organisationURL) {
          continue;
        }
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

      setResourcesGroup(data);
    }
    if (config.organisationURL) {
      getResources();
    }
  }, []);

  //Search hook
  useEffect(() => {
    let filtered = [];
    if (data) {
      filtered = search(data, searchTerms);
    }
    setShowProviders(filtered)
  }, [searchTerms,data]);

  //Match resource related providers when organisationURL is provided
  useEffect(() => {
    if (config.organisationURL) {
      const providers = getProvidersOfResources(resourcesGroup, config.organisationURL)
      setData(providersGroup.filter( item => checkProvider(item.id,providers)));
      setShowProviders(providersGroup.filter( item => checkProvider(item.id,providers)));
    }
    else {
      setData(providersGroup);
      setShowProviders(providersGroup);
    }
  }, [providersGroup,resourcesGroup]);

  return (
    <div className="container-fluid">
      <div className="mt-5">
        
        
        <h2 style={{color:config.colorA}} className="text-center title"><FontAwesomeIcon icon="university" style={{ color: config.colorA }} /> Providers</h2>

        <input
          className="form-control m-2 p-4 rounded col-6 mx-auto"
          type="text"
          placeholder="Search"
          value={searchTerms}
          onChange={handleChange}
        />
        <br />
      </div>

      <div className="row">{
        showProviders.map(item =>
          <ProviderItem
            key={item.id}
            id={item.id}
            title={item.epp_bai_2_abbreviation}
            img={item.epp_mri_2_logo}
            desc={item.epp_bai_1_name}
            tags={item.tags}
          />)}
      </div>
    </div>
  );
}

function ProviderItem(props) {
  

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
              <Link className="title" to={"/providers/" + props.id} style={{color:config.colorA}}>
                {props.title}
              </Link>
            </strong>
          </h6>
          {desc}

         
          
          <div className="mt-auto">
            <Link
              className="btn btn-dark btn-outline"
              to={"/providers/" + props.id}
            >
              View Provider
            </Link>
            { (props.tags.length > 0) && <hr/>}
            <TagItems items={props.tags} simple></TagItems>
          </div>
          

         

        </div>
      </div>
    </div>
  );
}


export default Providers;
