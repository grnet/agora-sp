import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Define Providers',
    Svg: require('@site/static/img/undraw_opened_tabs.svg').default,
    description: (
      <>
        Define your resource providers in great detail
      </>
    ),
  },
  {
    title: 'Specify Resources',
    Svg: require('@site/static/img/undraw_dropdown_menu.svg').default,
    description: (
      <>
         For each provider, specify the offered resources
      </>
    ),
  },
  {
    title: 'Share them with the world',
    Svg: require('@site/static/img/undraw_bibliophile.svg').default,
    description: (
      <>
        Share the information through a robust catalog service
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
