import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import config from "./config";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Collapse } from "reactstrap";
import getFlag from "./flags"
import ValueItem from "./ValueItem";
import TagItems from "./TagItems";
import RichItem from "./RichItem";


function Resource(props) {
  const [data, setData] = useState({});
  const params = useParams();
  const id = params.id;
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  useEffect(() => {
    async function getData() {
      const result = await axios(
        `${config.endpoint}/api/v2/public/resources/${id}`
      );
      let tags = [];
      let rloc = [];
      let loc = [];
      let lang = [];
      let rdata = result.data;
      if ("erp_cli_8_tags" in rdata && rdata.erp_cli_8_tags != null) {
        tags = rdata.erp_cli_8_tags.split(",").map((item) => item.trim());
      }
    
      if ("erp_rli_1_geographic_location" in rdata && rdata.erp_rli_1_geographic_location != null) {
        rloc = rdata.erp_rli_1_geographic_location.split(",").map((item) => item.trim());
      }

      if ("erp_gla_1_geographical_availability" in rdata && rdata.erp_gla_1_geographical_availability != null) {
        loc = rdata.erp_gla_1_geographical_availability.split(",").map((item) => item.trim());
      }

      if ("erp_gla_2_language" in rdata && rdata.erp_gla_2_language != null) {
        lang = rdata.erp_gla_2_language.split(",").map((item) => item.trim());
      }

      rdata["tags"] = tags;
      rdata["rloc"] = rloc;
      rdata["loc"] = loc;
      rdata["lang"] = lang; 
      setData(rdata);
    }

    getData();
  }, [id]);

  let logo = null;
  if (data.erp_mri_3_logo) {
    logo = (
      <img className="mw-75 biglogo" src={data.erp_mri_3_logo} alt="service logo" />
    );
  } else {
    logo = <FontAwesomeIcon icon="cloud" size="5x" style={{ color: "grey" }} />;
  }

  return (
    <div className="content mx-auto">
      <div className="text-center">
        {logo}
        <h2 style={{color:config.colorA}} className="title mt-3">{data.erp_bai_1_name}</h2>
        <h4>{data.erp_mri_2_tagline}</h4>
        <TagItems items={data.erp_bai_3_providers_public} valueOfKey="epp_bai_1_name" outline color="black"/>
      </div>
      <hr></hr>
      <div className="container-fluid">
        <div className="row">
          <div className="col-9">
            <div className="mb-2">
              <ValueItem
                icon="globe-americas"
                item={data.erp_bai_4_webpage}
                label="Official Website"
                link
                strong
                inline
              />

              <ValueItem
                icon="photo-video"
                item={data.erp_mri_4_multimedia}
                label="Multimedia"
                link
                strong
                inline
              />

              <ValueItem
                icon="book"
                item={data.erp_mri_5_use_cases}
                label="Use cases"
                link
                strong
                inline
              />

              {data.erp_mri_1_description && (
                <button className="down" onClick={toggle}>
                  ▼ {!isOpen && <small>show description</small>}
                </button>
              )}
            </div>

            
            <Collapse isOpen={isOpen}>
            <RichItem item={data.erp_mri_1_description} />
            </Collapse>
            <hr />

            <ContactInfo
              first_name={data.erp_coi_7_first_name}
              last_name={data.erp_coi_8_last_name}
              email={data.erp_coi_9_email}
              phone={data.erp_coi_10_phone}
              position={data.erp_coi_11_position}
              org={data.erp_coi_12_organization}
              helpdesk_email={data.erp_coi_13_helpdesk_email}
              security_email={data.erp_coi_14_security_contact_email}
            />

            <MaturityInfo
              tech={data.erp_mti_1_technology_readiness_level}
              lifecycle={data.erp_mti_2_lifecycle_status}
              certs={data.erp_mti_3_certifications}
              standards={data.erp_mti_4_standards}
              opensource={data.erp_mti_5_open_source_technologies}
              version={data.erp_mti_6_version}
              update={data.erp_mti_7_last_update}
              changelog={data.erp_mti_8_changelog}
            />

            <ManagementInfo
              helpdesk={data.erp_mgi_1_helpdesk_information}
              manual={data.erp_mgi_2_user_manual}
              terms={data.erp_mgi_3_terms_of_use}
              privacy={data.erp_mgi_4_privacy_policy}
              access={data.erp_mgi_5_access_policy}
              service={data.erp_mgi_6_service_level}
              training={data.erp_mgi_7_training_information}
              status={data.erp_mgi_8_status_monitoring}
              maintenance={data.erp_mgi_9_maintenance}
            />

            <DependenciesInfo
              required={data.erp_dei_1_required_resources_public}
              related={data.erp_dei_2_related_resources_public}
              platforms={data.erp_dei_3_related_platforms}
            />

            <AttributionsInfo
             program={data.erp_ati_1_funding_program}
             fund={data.erp_ati_2_funding_body}
             grant={data.erp_ati_3_grant_project_name}
            />

            <AccessOrderInfo
             orderType={data.erp_aoi_1_order_type}
             order={data.erp_aoi_2_order}
            />


            <FinancialInfo
             model={data.erp_fni_1_payment_model}
             pricing={data.erp_fni_1_pricing}
            />

           
            
           
          </div>

          <div className="col-lg-3 col-md-3">
            <TagsInfo tags={data.tags} />
            <ScientificInfo
              domains={data.erp_cli_1_scientific_domain}
              subdomains={data.erp_cli_2_scientific_subdomain}
            />
            <ResourceInfo
              categories={data.erp_cli_3_category}
              subcategories={data.erp_cli_4_subcategory}
            />
            <AccessInfo
              users={data.erp_cli_5_target_users}
              accessMode={data.erp_cli_6_access_mode}
              accessType={data.erp_cli_7_access_type}
            />
            <LocationInfo
              loc={data.loc}
              lang={data.lang}
              rloc={data.rloc}
            />
          </div>
        </div>
      </div>

      <div className="card-body"></div>
    </div>
  );
}


function AccessInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.users || props.users.length === 0) &&
    (!props.accessType || props.accessType.length === 0) &&
    (!props.accessMode || props.accessMode.length === 0)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="lock" />
      <strong>Access Classification</strong>{" "}
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
            items={props.users}
            label="Users"
            valueOfKey="user"
            breakpoint
          />
          <TagItems
            items={props.accessType}
            label="Access Type"
            valueOfKey="name"
          />
          <TagItems
            items={props.accessMode}
            label="Access Mode"
            valueOfKey="name"
          />
        </div>
      </Collapse>

      <hr />
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
      <FontAwesomeIcon className="mr-2" icon="atom" />
      <strong>Scientific</strong>{" "}
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
            label="Domains"
            valueOfKey="name"
            breakpoint
          />
          <TagItems
            items={props.subdomains}
            label="Subdomains"
            valueOfKey="name"
            breakpoint
          />
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function DependenciesInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.required || props.required.length === 0) &&
    (!props.related || props.related.length === 0) &&
    (!props.platforms)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="project-diagram" />
      <strong>Dependencies</strong>{" "}
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
            items={props.required}
            label="Required Resources"
            valueOfKey="erp_bai_1_name"
            breakpoint
          />
          <TagItems
            items={props.related}
            label="Related Resources"
            valueOfKey="erp_bai_1_name"
            breakpoint
          />
          <ValueItem
              item={props.platforms}              
              label="Related Platforms"
              strong
            />
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function AttributionsInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.program || props.program.length === 0) &&
    (!props.body || props.body.length === 0) &&
    (!props.grant)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="pen-fancy" />
      <strong>Attributions</strong>{" "}
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
            items={props.program}
            label="Funding Program"
            valueOfKey="name"
            breakpoint
          />
          <TagItems
            items={props.body}
            label="Funding Body"
            valueOfKey="name"
            breakpoint
          />
          <ValueItem
              item={props.grant}              
              label="Grant/Project Name"
              strong
            />
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function AccessOrderInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.orderType)  &&
    (!props.order)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="clipboard" />
      <strong>Access Order</strong>{" "}
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
          <ValueItem
              item={props.orderType}              
              label="Order Type"
              valueOfKey="name"
              strong
            />
          <ValueItem
              icon="clipboard"
              item={props.order}
              valueOfKey="name"              
              label="Order"
              link
              
          />
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function FinancialInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.model)  &&
    (!props.pricing)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="coins" />
      <strong>Fincancial Info</strong>{" "}
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
          <ValueItem
              icon = "book"
              item={props.orderType}              
              label="Payment Model"
              valueOfKey="name"
              link 
            />
          <ValueItem
              icon = "book"
              item={props.order}
              valueOfKey="name"              
              label="Pricing"
              link
          />
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
    (!props.loc || props.loc.length === 0) &&
    (!props.lang || props.lang.length === 0) &&
    (!props.rloc || props.rloc.length === 0)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="map-marker" />
      <strong>Location</strong>{" "}
      {!empty && (
        <button className="down" onClick={toggle}>
          ▼
        </button>
      )}
    </h5>
  );

  if (empty) return <div>{head}</div>;

  let langFlags = []
  for (let item of props.lang) {
    langFlags.push(item + " " + getFlag(item))
  }

  console.log(langFlags)

  return (
    <div>
      {head}
      <Collapse isOpen={isOpen}>
      <div className="ml-4">
          <TagItems
            items={props.loc}
            label="Locations"
            simple
            breakpoint
          />
          <TagItems
            items={langFlags}
            label="Languages"
            simple
            breakpoint
          />
          <TagItems
            items={props.rloc}
            label="Data Locations"
            simple
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
    !props.position &&
    !props.org &&
    !props.helpdesk_email &&
    !props.security_email
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
               <FontAwesomeIcon className=" pr-4 border-right" size="5x" icon="user" style={{color:config.colorA}} />
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
            <hr />
            <ValueItem
              item={"mailto:" + props.helpdesk_email}
              label="Helpdesk"
              link
              url={props.helpdesk_email}
              em
            />
            <ValueItem
              item={"mailto:" + props.security_email}
              label="Security Contact"
              link
              url={props.helpdesk_email}
              em
            />

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
    !props.tech &&
    !props.lifecycle &&
    !props.certs &&
    !props.standards &&
    !props.opensource &&
    !props.version &&
    !props.update &&
    !props.changelog
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
            <li><ValueItem item={props.tech} label="Technology Readiness Level" valueOfKey="name" strong /></li>
            <li><ValueItem item={props.lifecycle} label="Lifecycle Status" strong /></li>
            <li> <RichItem item={props.certs} label="Certifications" border /></li>
            <li> <RichItem item={props.standards} label="Standards" border /></li>
            <li><RichItem item={props.opensource} label="Open Source Technologies" border /></li>
            <li><ValueItem item={props.version} label="Version" strong /></li>
            <li><ValueItem item={props.update} label="Last Update" strong /></li>
            <li><RichItem item={props.changelog} label="Changelog" border /></li>
          </ul>
           
            
           
           
            
            
            
          
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

function ManagementInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    !props.helpdesk &&
    !props.manual &&
    !props.terms &&
    !props.privacy &&
    !props.access &&
    !props.service &&
    !props.training &&
    !props.status &&
    !props.maintenance
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="archive" />
      <strong>Management Information</strong>{" "}
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
          
          <br/>
          <ul className="list-unstyled">
            <li> <ValueItem icon="book" item={props.helpdesk} label="Helpdesk Information" link /></li>
            <li> <ValueItem icon="book" item={props.manual} label="User Manual" link /></li>
            <li> <ValueItem icon="book" item={props.terms} label="Terms of Service" link /></li>
            <li> <ValueItem icon="book" item={props.privacy} label="Privacy Policy" link /></li>
            <li> <ValueItem icon="book" item={props.access} label="Access Policy" link /></li>
            <li> <ValueItem icon="book" item={props.service} label="Service Level" link /></li>
            <li> <ValueItem icon="book" item={props.training} label="Training Information" link /></li>
            <li> <ValueItem icon="book" item={props.status} label="Status Monitoring" link /></li>
            <li> <ValueItem icon="book" item={props.maintenance} label="Maintenance" link /></li>
            
        
          </ul>
           
            
           
           
            
            
            
          
        </div>
      </Collapse>

      <hr />
    </div>
  );
}


function ResourceInfo(props) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  // get props.data
  let empty = false;

  if (
    (!props.categories || props.categories.length === 0) &&
    (!props.subcategories || props.subcategories.length === 0)
  ) {
    empty = true;
  }

  let head = (
    <h5 className={empty ? "xlight-grey" : "light-grey"}>
      <FontAwesomeIcon className="mr-2" icon="database" />
      <strong>Resources</strong>{" "}
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
            items={props.categories}
            label="Categories"
            valueOfKey="name"
            breakpoint
          />
          <TagItems
            items={props.subcategories}
            label="Subcategories"
            valueOfKey="name"
            breakpoint
          />
        </div>
      </Collapse>

      <hr />
    </div>
  );
}

export default Resource;
