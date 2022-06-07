import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import config from "./config";
import ValueItem from "./ValueItem";
import TagItems from "./TagItems";
import RichItem from "./RichItem";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Collapse } from "reactstrap";

function Provider(props) {
  const [data, setData] = useState({});
  const params = useParams();
  const [isOpen, setIsOpen] = useState(true);
  const toggle = () => setIsOpen(!isOpen);
  const id = params.id;

  useEffect(() => {
    async function getData() {
      const result = await axios(
        `${config.endpoint}/api/v2/public/providers/${id}`
      );
      let tags = [];
      let countries = [];
      let rdata = result.data;
      if ("epp_cli_tags" in rdata && rdata.epp_cli_tags != null) {
        tags = rdata.epp_cli_tags.split(",").map((item) => item.trim());
      }

      if (
        "epp_oth_participating_countries" in rdata &&
        rdata.epp_oth_participating_countries != null
      ) {
        countries = rdata.epp_oth_participating_countries
          .split(",")
          .map((item) => item.trim());
      }

      rdata["tags"] = tags;
      rdata["countries"] = countries;

      setData(rdata);
    }

    getData();
  }, [id]);

  let logo = null;
  if (data.epp_mri_logo) {
    logo = (
      <img className="mw-75 biglogo" src={data.epp_mri_logo} alt="service logo" />
    );
  } else {
    logo = <FontAwesomeIcon icon="cloud" size="5x" style={{ color: "grey" }} />;
  }

  return (
    <div className="content mx-auto">
      <div className="text-center">
        {logo}
        <h2 style={{ color: config.colorA }} className="title mt-3">
          {data.epp_bai_abbreviation}
        </h2>
        <h4>{data.epp_bai_name}</h4>
        <TagItems items={data.epp_bai_legal_status ? [data.epp_bai_legal_status] : []} valueOfKey="name" outline color="black"/>
      </div>
      <hr></hr>
      <div className="container-fluid">
        <div className="row">
          <div className="col-9">
            <div className="mb-2">
              <div className="mb-2">
                <ValueItem
                  icon="globe-americas"
                  item={data.epp_bai_website}
                  label="Official Website"
                  link
                  strong
                  inline
                />

                <ValueItem
                  icon="photo-video"
                  item={data.epp_mri_multimedia}
                  label="Multimedia"
                  link
                  strong
                  inline
                />

              {data.epp_mri_description && (
                <button className="down" onClick={toggle}>
                  ▼ {!isOpen && <small>show description</small>}
                </button>
              )}
              </div>

              <Collapse isOpen={isOpen} >
              <RichItem item={data.epp_mri_description} />
              </Collapse>
              <hr />

              <MaturityInfo
                lifecycle={data.epp_mti_life_cycle_status}
                certs={data.epp_mti_certifications}
              />
              
              <ContactInfo
                first_name={data.epp_coi_first_name}
                last_name={data.epp_coi_last_name}
                email={data.epp_coi_email}
                phone={data.epp_coi_phone}
                position={data.epp_coi_position}
              />

            <LocationInfo
                street={data.epp_loi_street_name_and_number}
                postal={data.epp_loi_postal_code}
                city={data.epp_loi_city}
                region={data.epp_loi_region}
                country={data.epp_loi_country_or_territory}
              />

            <OtherInfo
                hosting={data.epp_bai_hosting_legal_entity}
                countries={data.countries}
                affiliations={data.epp_oth_affiliations}
                networks={data.pp_oth_networks}
                structure={data.epp_cli_structure_type}
                activity={data.epp_oth_areas_of_activity}
                societal={data.epp_oth_societal_grand_challenges}
                roadmap={data.epp_loi_country_or_territory}
              />
            </div>

            
          </div>

          <div className="col-lg-3 col-md-3">
            <TagsInfo tags={data.tags} />
            <ScientificInfo
              icon="atom"
              title="Scientific"
              domLabel="Domain"
              subLabel="Subdomain"
              domains={data.epp_cli_scientific_domain}
              subdomains={data.epp_cli_scientific_subdomain}
            />
            <ScientificInfo
              icon="flask"
              title="MERIL"
              domLabel="Domain"
              subLabel="Subdomain"
              domains={data.epp_oth_meril_scientific_domain}
              subdomains={data.epp_oth_meril_scientific_subdomain}
            />
            <ScientificInfo
              icon="microscope"
              title="ESFRI"
              domLabel="Domain"
              subLabel="Type"
              domains={data.epp_oth_esfri_domain}
              subdomains={data.epp_oth_esfri_type ? [data.epp_oth_esfri_type] : []}
            />
          </div>
        </div>
      </div>

      <div className="card-body"></div>
    </div>
  );
}

function TagsInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (!props.tags || props.tags.length === 0) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="tag" />
      <strong>Tags</strong>{" "}
      {!empty && (
        <button className="down" onClick={toggle}>
          ▼
        </button>
      )}
    </h5>
  );

  if (empty) return <div>{head}</div>;

  return (
    <div>
      {head}
      <Collapse isOpen={isOpen}>
        <div className="ml-4">
          <TagItems items={props.tags} label="" simple breakpoint />
        </div>
      </Collapse>

      <hr />
    </div>
  );
}


function ScientificInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.domains || props.domains.length === 0) &&
    (!props.subdomains || props.subdomains.length === 0)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon={props.icon} />
      <strong>{props.title}</strong>{" "}
      {!empty && (
        <button className="down" onClick={toggle}>
          ▼
        </button>
      )}
    </h5>
  );

  if (empty) return <div>{head}</div>;

  return (
    <div>
      {head}
      <Collapse isOpen={isOpen}>
        <div className="ml-4">
          <TagItems
            items={props.domains}
            label={props.domLabel}
            valueOfKey="name"
            breakpoint
          />
          <TagItems
            items={props.subdomains}
            label={props.subLabel}
            valueOfKey="name"
            breakpoint
          />
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function ContactInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    !props.first_name &&
    !props.last_name &&
    !props.email &&
    !props.phone &&
    !props.position
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="user" />
      <strong>Contact Info</strong>{" "}
      {!empty && (
        <button className="down" onClick={toggle}>
          ▼
        </button>
      )}
    </h5>
  );

  if (empty) return <div>{head}</div>;

  return (
    <div>
      {head}
      <Collapse isOpen={isOpen}>
        <div className="row">
          <div className="shadow col-md-auto col2 p-4 ml-5 mt-2 border-dark border rounded bcard">
            <div className="row">
              <div className="col2 p-4">
               <FontAwesomeIcon className=" pr-4 border-right" size="5x" icon="user" style={{color:config.colorA}}  />
              </div>
              <div className="col2 p-3">
              <ValueItem item={props.first_name} inline />{" "}
            <ValueItem item={props.last_name} inline />
            <ValueItem
              icon="envelope"
              item={"mailto:" + props.email}
              link
              url={props.email}
            />
            <ValueItem
              icon="phone"
              item={"tel:" + props.phone}
              link
              url={props.phone}
            />
            <ValueItem item={props.position} label="Position" strong />
            <ValueItem item={props.org} label="Organization" />
              </div>
            </div>
            
          </div>
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function LocationInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    !props.street &&
    !props.postal &&
    !props.city &&
    !props.region &&
    !props.country
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="map-marker" />
      <strong>Location Info</strong>{" "}
      {!empty && (
        <button className="down" onClick={toggle}>
          ▼
        </button>
      )}
    </h5>
  );

  if (empty) return <div>{head}</div>;

  return (
    <div>
      {head}
      <Collapse isOpen={isOpen}>
        <div className="row">
          <div className="shadow col-md-auto col2 p-4 ml-5 mt-2 border-dark border rounded bcard">
            <div className="row">
              <div className="col2 p-4">
               <FontAwesomeIcon className=" pr-4 border-right" size="5x" icon="map-marked-alt" style={{color:config.colorA}}  />
              </div>
              <div className="col2 p-3">
              <ValueItem item={props.street} em />
            <ValueItem item={props.postal} />
            <ValueItem item={props.city} />
            <ValueItem item={props.region}  />
            <ValueItem item={props.country} strong />
              </div>
            </div>
            
          </div>
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function MaturityInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    !props.lifecycle &&
    !props.certs 
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="trophy" />
      <strong>Maturity Information</strong>{" "}
      {!empty && (
        <button className="down" onClick={toggle}>
          ▼
        </button>
      )}
    </h5>
  );

  if (empty) return <div>{head}</div>;

  return (
    <div>
      {head}
      <Collapse isOpen={isOpen}>
        <div className="ml-4">
          
          <ul className="list-unstyled">
            <li><ValueItem item={props.lifecycle} label="Lifecycle Status" strong breakpoint /></li>
            <li> <ValueItem item={props.certs} label="Certifications" strong breakpoint /></li>
          </ul>
           
            
           
           
            
            
            
          
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function OtherInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.hosting) &&
    (!props.countries || props.countries.length === 0) && 
    (!props.affiliations || props.affiliations.length === 0) && 
    (!props.networks || props.networks.length === 0) && 
    (!props.sctructure || props.structure.length === 0) && 
    (!props.activity || props.activity.length === 0) && 
    (!props.societal || props.societal.length === 0) && 
    (!props.roadmap)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="info-circle" />
      <strong>Other Information</strong>{" "}
      {!empty && (
        <button className="down" onClick={toggle}>
          ▼
        </button>
      )}
    </h5>
  );

  if (empty) return <div>{head}</div>;

  return (
    <div>
      {head}
      <Collapse isOpen={isOpen}>
        <div className="ml-4">
          
          <ul className="list-unstyled">
            <li><ValueItem item={props.hosting} label="Hosting Legal Entity" strong breakpoint /></li>
            <li> 
              <TagItems
                items={props.countries}
                label="Participating Countries"
                simple
                breakpoint
              />
            </li>
            <li> 
              <TagItems
                items={props.affiliations}
                label="Affiliations"
                valueOfKey="name"
                breakpoint
              />
            </li>
            <li> 
              <TagItems
                items={props.networks}
                label="Networks"
                valueOfKey="name"
                breakpoint
              />
            </li>
            <li> 
              <TagItems
                items={props.structure}
                label="Structure"
                valueOfKey="name"
                breakpoint
              />
            </li>
            <li> 
              <TagItems
                items={props.activity}
                label="Activity"
                valueOfKey="name"
                breakpoint
              />
            </li>
            <li> 
              <TagItems
                items={props.societal}
                label="Societal Grand Challenges"
                valueOfKey="name"
                breakpoint
              />
            </li>
            <li><ValueItem item={props.roadmap} label="National Roadmaps" strong breakpoint /></li>
          </ul>
           
            
           
           
            
            
            
          
        </div>
      </Collapse>

      <hr />
    </div>
  );
}



export default Provider;
