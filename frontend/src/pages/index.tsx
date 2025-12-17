import { useCallback } from "react";
import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';
import Particles from "@tsparticles/react";
import { loadFull } from "tsparticles";
import type { Engine } from "@tsparticles/engine";
import particlesOptions from "@site/src/tsparticles-config.json";
import ChatWidget from '@site/src/components/ChatBot';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const particlesInit = useCallback(async (engine: Engine) => {
    await loadFull(engine);
  }, []);
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner, styles.heroGlow)}>
      <Particles
        id="tsparticles"
        init={particlesInit}
        options={particlesOptions}
        className={styles.particles}
      />
      <div className={clsx("container", styles.heroContainer)}>
        <div className="row">
          <div className="col col--6">
            <Heading as="h1" className="hero__title">
              {siteConfig.title}
            </Heading>
            <p className="hero__subtitle">{siteConfig.tagline}</p>
            <div className={styles.buttons}>
              <Link
                className="button button--secondary button--lg"
                to="/docs/intro">
                Start Learning Robotics
              </Link>
              <Link
                className="button button--info button--lg"
                to="/blog">
                Explore the Blog
              </Link>
            </div>
          </div>
          <div className="col col--6">
            <img src="img/robot_ai.png" alt="AI Robot" className={styles.heroImage} />
          </div>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to the Future of Robotics | ${siteConfig.title}`}
      description="Your premier resource for mastering Physical AI and Humanoid Robotics with cutting-edge simulations and AI-native features.">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
      <div style={{ position: 'fixed', bottom: '20px', right: '20px', zIndex: 1000 }}>
        <ChatWidget />
      </div>
    </Layout>
  );
}
