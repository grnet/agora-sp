import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import config from "./config";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import search from "./search";
import TagItems from "./TagItems";

const getProvidersOfResources = (resources, orgURL) => {
  let providers = [orgURL]
  for (let resource of resources ) {
    if (!!resource.erp_bai_providers_public){
      for( let provider of resource.erp_bai_providers_public){
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
        `${config.endpoint}/api/v2/public/providers/`
      );
      let data = [];
      for (let item of result.data) {
        let terms = [];
        let tags = [];
        if ("epp_bai_name" in item && item.epp_bai_name != null) {
          terms.push(item.epp_bai_name.toLowerCase());
        }
        if ("epp_bai_abbreviation" in item && item.epp_bai_abbreviation != null) {
          terms.push(item.epp_bai_abbreviation.toLowerCase());
        }
        if ("epp_cli_tags" in item && item.epp_cli_tags != null) {
          tags = item.epp_cli_tags.split(",").map((item) => item.trim());
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

  // Get resources if organisationUUID is specified
  useEffect(() => {
    async function getResources() {
      let AGORA_URL = `${config.endpoint}/api/v2/public/resources/`
      if (!!config.organisationUUID) {
        AGORA_URL = AGORA_URL + '?erp_bai_organisation=' + config.organisationUUID
      }
      const result = await axios(
        AGORA_URL
      );
      let data = [];
      for (let item of result.data) {
        let terms = [];
        let tags = [];
        if ("erp_bai_name" in item && item.erp_bai_name != null) {
          terms.push(item.erp_bai_name.toLowerCase());
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
    if (!!config.organisationUUID) {
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

  //Match resource related providers when organisationUUID is provided
  useEffect(() => {
    if (!!config.organisationUUID) {
      const providers = getProvidersOfResources(resourcesGroup, `${config.endpoint}/api/v2/public/providers/${config.organisationUUID}`)
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
            title={item.epp_bai_abbreviation}
            img={item.epp_mri_2_logo}
            desc={item.epp_bai_name}
            tags={item.tags}
          />)}
      </div>
    </div>
  );
}

function ProviderItem(props) {
  

  let logo = null;
  if (props.img) {
    let logo_style = {
      maxHeight: !!config.miniLogoMaxHeight? config.miniLogoMaxHeight: 65,
      maxWidth: !!config.miniLogoMaxWidth? config.miniLogoMaxWidth: 150,
    }
    logo = <img style={logo_style} className="mw-75 logo" src={props.img} alt="service logo" />;
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
          <h5>
            <strong>
              <Link className="title" to={"/providers/" + props.id} style={{color:config.colorA}}>
                {props.title}
              </Link>
            </strong>
          </h5>
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
