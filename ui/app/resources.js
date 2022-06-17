const countries = [
'Afghanistan (AF)',
'Åland Islands (AX)',
'Albania (AL)',
'Algeria (DZ)',
'American Samoa (AS)',
'Andorra (AD)',
'Angola (AO)',
'Anguilla (AI)',
'Antarctica (AQ)',
'Antigua and Barbuda (AG)',
'Argentina (AR)',
'Armenia (AM)',
'Aruba (AW)',
'Australia (AU)',
'Austria (AT)',
'Azerbaijan (AZ)',
'Bahamas (BS)',
'Bahrain (BH)',
'Bangladesh (BD)',
'Barbados (BB)',
'Belarus (BY)',
'Belgium (BE)',
'Belize (BZ)',
'Benin (BJ)',
'Bermuda (BM)',
'Bhutan (BT)',
'Bolivia (BO)',
'Bonaire, Sint Eustatius and Saba (BQ)',
'Bosnia and Herzegovina (BA)',
'Botswana (BW)',
'Bouvet Island (BV)',
'Brazil (BR)',
'British Indian Ocean Territory (IO)',
'Brunei Darussalam (BN)',
'Bulgaria (BG)',
'Burkina Faso (BF)',
'Burundi (BI)',
'Cabo Verde (CV)',
'Cambodia (KH)',
'Cameroon (CM)',
'Canada (CA)',
'Cayman Islands (KY)',
'Central African Republic (CF)',
'Chad (TD)',
'Chile (CL)',
'China (CN)',
'Christmas Island (CX)',
'Cocos - Keeling - Islands (CC)',
'Colombia (CO)',
'Comoros (KM)',
'Congo - Democratic Republic (CD)',
'Congo (CG)',
'Cook Islands (CK)',
'Costa Rica (CR)',
'Côte d’Ivoire (CI)',
'Croatia (HR)',
'Cuba (CU)',
'Curaçao (CW)',
'Cyprus (CY)',
'Czechia (CZ)',
'Denmark (DK)',
'Djibouti (DJ)',
'Dominica (DM)',
'Dominican Republic (DO)',
'Ecuador (EC)',
'Egypt (EG)',
'El Salvador (SV)',
'Equatorial Guinea (GQ)',
'Eritrea (ER)',
'Estonia (EE)',
'Eswatini (SZ)',
'Ethiopia (ET)',
'Falkland Islands (FK)',
'Faroe Islands (FO)',
'Fiji (FJ)',
'Finland (FI)',
'France (FR)',
'French Guiana (GF)',
'French Polynesia (PF)',
'French Southern Territories (TF)',
'Gabon (GA)',
'Gambia (GM)',
'Georgia (GE)',
'Germany (DE)',
'Ghana (GH)',
'Gibraltar (GI)',
'Greece (EL)',
'Greenland (GL)',
'Grenada (GD)',
'Guadeloupe (GP)',
'Guam (GU)',
'Guatemala (GT)',
'Guernsey (GC)',
'Guinea (GN)',
'Guinea-Bissau (GW)',
'Guyana (GY)',
'Haiti (HT)',
'Heard Island and McDonald Islands (HM)',
'Holy See (VA)',
'Honduras (HN)',
'Hong Kong (HK)',
'Hungary (HU)',
'Iceland (IS)',
'India (IN)',
'Indonesia (ID)',
'Iran (IR)',
'Iraq (IQ)',
'Ireland (IE)',
'Isle of Man (IM)',
'Israel (IL)',
'Italy (IT)',
'Jamaica (JM)',
'Japan (JP)',
'Jersey (JE)',
'Jordan (JO)',
'Kazakhstan (KZ)',
'Kenya (KE)',
'Kiribati (KI)',
'Korea - Democratic People\'s Republic (KP)',
'Korea - Republic (KR)',
'Kuwait (KW)',
'Kyrgyzstan (KG)',
'Lao People\'s Democratic Republic (LA)',
'Latvia (LV)',
'Lebanon (LB)',
'Lesotho (LS)',
'Liberia (LR)',
'Libya (LY)',
'Liechtenstein (LI)',
'Lithuania (LT)',
'Luxembourg (LU)',
'Macao (MO)',
'Madagascar (MG)',
'Malawi (MW)',
'Malaysia (MY)',
'Maldives (MV)',
'Mali (ML)',
'Malta (MT)',
'Marshall Islands (MH)',
'Martinique (MQ)',
'Mauritania (MR)',
'Mauritius (MU)',
'Mayotte (YT)',
'Mexico (MX)',
'Micronesia (FM)',
'Moldova (MD)',
'Monaco (MC)',
'Mongolia (MN)',
'Montenegro (ME)',
'Montserrat (MS)',
'Morocco (MA)',
'Mozambique (MZ)',
'Myanmar (MM)',
'Namibia (NA)',
'Nauru (NR)',
'Nepal (NP)',
'Netherlands (NL)',
'New Caledonia (NC)',
'New Zealand (NZ)',
'Nicaragua (NI)',
'Niger (NE)',
'Nigeria (NG)',
'Niue (NU)',
'Norfolk Island (NF)',
'North Macedonia (MK)',
'Northern Mariana Islands (MP)',
'Norway (NO)',
'Oman (OM)',
'Pakistan (PK)',
'Palau (PW)',
'Palestine, State of (PS)',
'Panama (PA)',
'Papua New Guinea (PG)',
'Paraguay (PY)',
'Peru (PE)',
'Philippines (PH)',
'Pitcairn (PN)',
'Poland (PL)',
'Portugal (PT)',
'Puerto Rico (PR)',
'Qatar (QA)',
'Réunion (RE)',
'Romania (RO)',
'Russian Federation (RU)',
'Rwanda (RW)',
'Saint Barthélemy (BL)',
'Saint Helena, Ascension and Tristan da Cunha (SH)',
'Saint Kitts and Nevis (KN)',
'Saint Lucia (LC)',
'Saint Martin (MF)',
'Saint Pierre and Miquelon (PM)',
'Saint Vincent and the Grenadines (VC)',
'Samoa (WS)',
'San Marino (SM)',
'São Tomé and Príncipe (ST)',
'Saudi Arabia (SA)',
'Senegal (SN)',
'Serbia (RS)',
'Seychelles (SC)',
'Sierra Leone (SL)',
'Singapore (SG)',
'Sint Maarten (SX)',
'Slovakia (SK)',
'Slovenia (SI)',
'Solomon Islands (SB)',
'Somalia (SO)',
'South Africa (ZA)',
'South Georgia and the South Sandwich Islands (GS)',
'South Sudan (SS)',
'Spain (ES)',
'Sri Lanka (LK)',
'Sudan (SD)',
'Suriname (SR)',
'Svalbard and Jan Mayen (SJ)',
'Sweden (SE)',
'Switzerland (SH)',
'Syrian Arab Republic (SY)',
'Taiwan (Province of China) (TW)',
'Tajikistan (TJ)',
'Tanzania (TZ)',
'Thailand (TH)',
'Timor-Leste (TL)',
'Togo (TG)',
'Tokelau (TK)',
'Tonga (YO)',
'Trinidad and Tobago (TT)',
'Tunisia (TN)',
'Turkey (TR)',
'Turkmenistan (TM)',
'Turks and Caicos Islands (TC)',
'Tuvalu (TV)',
'Uganda (UG)',
'Ukraine (UA)',
'United Arab Emirates (AE)',
'United Kingdom of Great Britain and Northern Ireland (UK)',
'United States Minor Outlying Islands (UM)',
'United States of America (US)',
'Uruguay (UY)',
'Uzbekistan (UZ)',
'Vanuatu (VU)',
'Venezuela (VE)',
'Viet Nam (VN)',
'Virgin Islands (British) (VG)',
'Virgin Islands (U.S.) (VI)',
'Wallis and Futuna (WF)',
'Western Sahara (EH)',
'Yemen (YE)',
'Zambia (ZM)',
'Zimbabwe (ZW)'
];

const disciplines = [
  'Accelerator physics',
  'Acoustics',
  'Aerobiology',
  'Aeronautical engineering',
  'Aerosol physics',
  'Aerospace engineering',
  'Agricultural Sciences',
  'Agricultural biotechnology',
  'Agriculture',
  'Agriculture forestry and fisheries',
  'Agronomy/plant breeding/plant protection',
  'Algorithms',
  'Allergy',
  'Anaesthesiology',
  'Analytical chemistry',
  'Anatomy and morphology',
  'Andrology',
  'Animal and dairy sciences',
  'Animal science',
  'Anthropology',
  'Applied mechanics',
  'Archaeology',
  'Architectural design',
  'Architecture engineering',
  'Artificial Intelligence (expert systems\,machine learning\, robotics)',
  'Arts',
  'Astrobiology',
  'Astronautical engineering',
  'Astronomy',
  'Astroparticle physics',
  'Astrophysics',
  'Atmospheric science',
  'Atomic',
  'Audio engineering',
  'Bacteriology',
  'Basic medicine',
  'Behavioural biology',
  'Bio-derived novel materials',
  'Biocatalysis',
  'Biochemistry and molecular biology',
  'Bioderived bulk and fine chemicals',
  'Biodiversity conservation',
  'Bioengineering',
  'Bioengineering and Biomedical engineering',
  'Biofuels',
  'Bioinformatics',
  'Biological Psychology',
  'Biological rhythm',
  'Biology',
  'Biomass feedstock production tech.',
  'Biomaterials',
  'Biomedical devices',
  'Biomedical engineering',
  'Biopharming',
  'Biophysical manipulation',
  'Biophysics',
  'Bioprocessing technologies',
  'Bioproducts',
  'Bioremediation',
  'Biotechnology and medical ethics',
  'Botany',
  'Business and Management',
  'Canon Law',
  'Cardiac and Cardiovascular systems',
  'Cell biology',
  'Ceramics',
  'Chemical engineering',
  'Chemical engineering (plants/products)',
  'Chemical physics',
  'Chemical process engineering',
  'Chemistry',
  'Civil Law',
  'Civil Protection',
  'Civil engineering',
  'Climate research',
  'Clinical Psychology',
  'Clinical medicine',
  'Coating and films',
  'Cognitive Psychology',
  'Colloid chemistry',
  'Communication engineering and systems',
  'Comparative Law',
  'Comparative Psychology',
  'Comparative politics',
  'Competition Law',
  'Composites',
  'Computational biology',
  'Computational chemistry',
  'Computational physics',
  'Computer architecture',
  'Computer communications',
  'Computer graphics',
  'Computer hardware and architecture',
  'Computer security and reliability',
  'Condensed matter physics',
  'Constitutional Law',
  'Construction/Structural engineering',
  'Criminal Law',
  'Critical care/Emergency medicine',
  'Cryobiology',
  'Cryogenics',
  'Cultural and economic geography',
  'Dairy science',
  'Data management',
  'Data mining',
  'Data structures',
  'Demography',
  'Dentistry, oral surgery/medicine',
  'Dermatology and venereal diseases',
  'Developmental Psychology',
  'Developmental biology',
  'Diagnostic biotechnologies',
  'Diagnostics',
  'Distributed computing',
  'Ecology',
  'Economics and Econometrics',
  'Economics finance and business',
  'Educational and School Psychology',
  'Educational sciences',
  'Electrical and electronic engineering',
  'Electrical, electronic and information engineering',
  'Electrochemistry',
  'Empirical pata analysis',
  'Energy and fuels',
  'Environmental biotechnology',
  'Environmental engineering',
  'Epidemiology',
  'Ethics',
  'Ethnology',
  'Evolutionary Psychology',
  'Evolutionary biology',
  'Family studies',
  'Fermentation',
  'Finance',
  'Fishery',
  'Fluid Mechanics',
  'Folklore studies',
  'Food biotechnology',
  'Forestry',
  'Fusion',
  'GM technology (crops/livestock)',
  'Gastroenterology and hepatology',
  'General Education',
  'General and internal medicine',
  'General language studies',
  'General literature studies',
  'Genetics and heredity',
  'Geochemistry',
  'Geological engineering',
  'Geology',
  'Geophysics',
  'Geotechnics',
  'Geriatrics and gerontology',
  'Health care science and services',
  'Health policy and services',
  'Health sciences',
  'Health-related biotechnology',
  'Hematology',
  'High energy physics',
  'History (Prehistory; Ancient; Modern world)',
  'History and Archaeology',
  'Horticulture and viticulture',
  'Human genetics',
  'Human-computer interaction',
  'Humanities',
  'Husbandry',
  'Hydrology',
  'Immunology',
  'Industrial biotechnology',
  'Industrial relations',
  'Industrial–organisational Psychology',
  'Infectious diseases',
  'Information management',
  'Information retrieval',
  'Information science - social',
  'Inorganic and nuclear chemistry',
  'Integrative and Complementary medicine',
  'International relations',
  'Islamic Law',
  'Jewish Law',
  'Journalism',
  'Jurisprudence (Philosophy of Law)',
  'Knowledge management',
  'Languages and literature',
  'Law',
  'Library science',
  'Linguistics',
  'Literary theory',
  'Livestock cloning',
  'Marine and Freshwater biology',
  'Marker assisted selection',
  'Materials engineering',
  'Mathematical biology',
  'Mathematical chemistry',
  'Mathematical physics',
  'Mechanical engineering',
  'Media Studies (Film/Radio/TV)',
  'Media and communications',
  'Media and socio-cultural communication',
  'Medical and Health Sciences',
  'Medical biotechnology',
  'Medical ethics',
  'Medical imaging',
  'Medical physics',
  'Medicinal chemistry',
  'Microbiology',
  'Mineralogy',
  'Mining and mineral processing',
  'Molecular diagnostics',
  'Molecular physics',
  'Multimedia/hypermedia',
  'Musicology',
  'Mycology',
  'Nano-materials',
  'Nano-processes',
  'Nano-technology',
  'Neuroscience',
  'Nuclear medicine',
  'Nuclear physics',
  'Nuclear related engineering',
  'Nursing',
  'Nutrition and Dietetics',
  'Obstetrics and gynaecology',
  'Occupational health',
  'Ocean engineering',
  'Oceanography',
  'Oncology',
  'Operating systems',
  'Ophthalmology',
  'Optics',
  'Optometry',
  'Organic chemistry',
  'Organisation theory',
  'Orthopaedics',
  'Other',
  'Otorhinolaryngology',
  'Paediatrics',
  'Palaeontology',
  'Paper and wood',
  'Parallel computing',
  'Parasitology',
  'Particle physics',
  'Pathology',
  'Performing arts studies',
  'Peripheral vascular disease',
  'Personality Psychology',
  'Petroleum engineering',
  'Pets',
  'Pharmaceutical biotechnology',
  'Pharmacology and pharmacy',
  'Philosophy',
  'Philosophy ethics and religion',
  'Philosophy of science/technology',
  'Physical chemistry',
  'Physical geography',
  'Physics',
  'Physiology',
  'Planetary science',
  'Plant science',
  'Plasma physics',
  'Political economy',
  'Political philosophy',
  'Political sciences',
  'Polymer science',
  'Positive Psychology',
  'Programming languages',
  'Psychiatry',
  'Psychology',
  'Public administration',
  'Public and environmental health',
  'Pure mathematics',
  'Quantum computing',
  'Quantum physics',
  'Radiology',
  'Reliability analysis',
  'Religious studies',
  'Remote sensing',
  'Reproductive biology',
  'Respiratory systems',
  'Rheumatology',
  'Robotics Automation and Control Systems',
  'Sea vessels',
  'Seismology',
  'Social Psychology',
  'Social Sciences',
  'Social and economic geography',
  'Social biomedical science',
  'Social issues',
  'Social work',
  'Sociology',
  'Sociology',
  'Software engineering',
  'Soil science',
  'Space science',
  'Special Education (learning disabilities)',
  'Specific languages',
  'Specific literatures',
  'Sport and fitness science',
  'Statistics and probability',
  'Structural biology',
  'Substance abuse',
  'Surgery',
  'Taxonomy',
  'Textiles',
  'Theology',
  'Theoretical biology',
  'Theories of the state',
  'Theory of computation',
  'Thermal biology',
  'Thermodynamics',
  'Toxicology',
  'Transplantation',
  'Transport engineering',
  'Transport planning',
  'Tropical medicine',
  'Urban studies',
  'Urology and nephrology',
  'Veterinary anaesthesiology',
  'Veterinary medicine',
  'Veterinary ophthalmology',
  'Veterinary pathobiology',
  'Veterinary radiology',
  'Veterinary reproduction',
  'Veterinary sciences',
  'Veterinary surgery',
  'Virology',
  'Volcanology',
  'Women\'s and gender studies',
  'Zoology',
];

const language_codes = [
  'ab',
  'aa',
  'af',
  'ak',
  'sq',
  'am',
  'ar',
  'an',
  'hy',
  'as',
  'av',
  'ae',
  'ay',
  'az',
  'bm',
  'ba',
  'eu',
  'be',
  'bn',
  'bh',
  'bi',
  'bs',
  'br',
  'bg',
  'my',
  'ca',
  'km',
  'ch',
  'ce',
  'ny',
  'zh',
  'cu',
  'cv',
  'kw',
  'co',
  'cr',
  'hr',
  'cs',
  'da',
  'dv',
  'nl',
  'dz',
  'en',
  'eo',
  'et',
  'ee',
  'fo',
  'fj',
  'fi',
  'fr',
  'ff',
  'gd',
  'gl',
  'lg',
  'ka',
  'de',
  'el',
  'gn',
  'gu',
  'ht',
  'ha',
  'he',
  'hz',
  'hi',
  'ho',
  'hu',
  'is',
  'io',
  'ig',
  'id',
  'ia',
  'ie',
  'iu',
  'ik',
  'ga',
  'it',
  'ja',
  'jv',
  'kl',
  'kn',
  'kr',
  'ks',
  'kk',
  'ki',
  'rw',
  'ky',
  'kv',
  'kg',
  'ko',
  'kj',
  'ku',
  'lo',
  'la',
  'lv',
  'li',
  'ln',
  'lt',
  'lu',
  'lb',
  'mk',
  'mg',
  'ms',
  'ml',
  'mt',
  'gv',
  'mi',
  'mr',
  'mh',
  'mn',
  'na',
  'nv',
  'ng',
  'ne',
  'nd',
  'se',
  'no',
  'nb',
  'nn',
  'oc',
  'oj',
  'or',
  'om',
  'os',
  'pi',
  'ps',
  'fa',
  'pl',
  'pt',
  'pa',
  'qu',
  'ro',
  'rm',
  'rn',
  'ru',
  'sm',
  'sg',
  'sa',
  'sc',
  'sr',
  'sn',
  'ii',
  'sd',
  'si',
  'sk',
  'sl',
  'so',
  'nr',
  'st',
  'es',
  'su',
  'sw',
  'ss',
  'sv',
  'tl',
  'ty',
  'tg',
  'ta',
  'tt',
  'te',
  'th',
  'bo',
  'ti',
  'to',
  'ts',
  'tn',
  'tr',
  'tk',
  'tw',
  'ug',
  'uk',
  'ur',
  'uz',
  've',
  'vi',
  'vo',
  'wa',
  'cy',
  'fy',
  'wo',
  'xh',
  'yi',
  'yo',
  'za',
  'zu',
];

const areas = [
  'Worldwide (WW)',
  'Europe (EO)',
  'European Union (EU)',
  'Euro Zone (EZ)',
  'Schengen Area (AH)',
];


const locations = countries.concat(areas)

export {
  countries,
  locations,
  disciplines,
  language_codes,
}
