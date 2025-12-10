import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Tutorial Basics',
      link: {
        type: 'generated-index',
        title: 'Tutorial Basics',
        description: 'Learn the foundational concepts of Physical AI and Humanoid Robotics.',
        slug: '/category/tutorial-basics',
      },
      items: [
        'tutorial-basics/create-a-document',
        // CORRECTED: Removed '03-' prefix
        'tutorial-basics/urdf-robot-description',
        'tutorial-basics/Tutorial 4 Gazebo Simulation',
        // CORRECTED: Removed '05-' prefix
        'tutorial-basics/isaac-sim-basics',
        // CORRECTED: Removed '07-' prefix
        'tutorial-basics/conversational-robotics',
        // CORRECTED: Removed '08-' prefix
        'tutorial-basics/capstone-humanoid',
        'tutorial-basics/congratulations',
      ],
    },
    {
      type: 'category',
      label: 'Advanced Topics',
      link: {
        type: 'generated-index',
        title: 'Advanced Topics',
        description: 'Dive deeper into advanced concepts and techniques.',
        slug: '/category/advanced-topics',
      },
      items: [
        // CORRECTED: Removed '09-' prefix
        'tutorial-extras/advanced-ros2',
        // CORRECTED: Removed '10-' prefix
        'tutorial-extras/gazebo-advanced-physics',
        // CORRECTED: Removed '11-' prefix
        'tutorial-extras/reinforcement-learning-humanoids',
        // CORRECTED: Removed '12-' prefix
        'tutorial-extras/advanced-isaac-sim-usd',
        // CORRECTED: Removed '13-' prefix
        'tutorial-extras/advanced-sensor-fusion',
        // CORRECTED: Removed '14-' prefix
        'tutorial-extras/whole-body-control',
      ],
    },
  ],
};

export default sidebars;