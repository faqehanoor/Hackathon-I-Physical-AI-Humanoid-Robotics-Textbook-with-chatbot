import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import { FaRobot, FaBrain, FaBookOpen } from 'react-icons/fa';

type FeatureItem = {
  title: string;
  Icon: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Physical AI Ready',
    Icon: FaRobot,
    description: (
      <>
         Build real-world intelligent systems with a textbook deeply integrated
        into robotics simulation, humanoid control, and embodied AI principles.
      </>
    ),
  },
  {
    title: 'Simulation First Learning',
    Icon: FaBrain,
    description: (
      <>
         Learn humanoid robotics through hands-on labs using ROS 2, Gazebo,
        and NVIDIA Isaac Sim—designed for real-world training and digital twins.
      </>
    ),
  },
  {
    title: 'AI-Native Textbook',
    Icon: FaBookOpen,
    description: (
      <>
        Your book includes RAG chatbot support, Urdu translation, personalization,
        subagents, and interactive MDX components powered by React & AI.
      </>
    ),
  },
];

function Feature({title, Icon, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className={clsx('card', styles.featureCard)}>
        <div className="text--center">
          <Icon className={styles.featureIcon} />
        </div>
        <div className="text--center padding-horiz--md">
          <Heading as="h3">{title}</Heading>
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
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
