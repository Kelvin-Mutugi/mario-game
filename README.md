# learnpygame 🎮

A collaborative Pygame project for learning and building fun games together!

## About This Project

**learnpygame** is an open, beginner-friendly game development project built with Python and Pygame. Whether you're new to game development or looking to contribute features, this is the perfect place to learn, collaborate, and have fun.

## Project Goals

- Learn Pygame fundamentals through hands-on development
- Build an engaging, feature-rich game collaboratively
- Create a welcoming space for contributors of all skill levels
- Keep code clean, modular, and well-documented

## Getting Started

### Prerequisites
- Python 3.8+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd learnpygame
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install pygame
   ```

4. Run the game:
   ```bash
   python main.py
   ```

## How to Contribute

### Getting Started with Development

1. Fork the repository (or request contributor access)
2. Create a feature branch with a descriptive name:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes with clear, focused commits
4. Push and open a Pull Request with a description of your changes

### Feature Ideas to Work On

- **Visual Improvements** — Add animations, particle effects, better sprites
- **Gameplay Mechanics** — Power-ups, level systems, difficulty scaling
- **Audio & Sound** — Background music, sound effects, audio feedback
- **Scoring & Stats** — Leaderboards, achievements, game statistics
- **UI/UX** — Main menu, pause screen, settings menu
- **AI Improvements** — Smarter enemy behavior, boss mechanics
- **Mobile Support** — Touch controls, responsive design

### Contribution Guidelines

- **Branch Naming:** Use `feature/`, `fix/`, or `docs/` prefixes
  - Example: `feature/power-ups`, `fix/collision-bug`
- **Commits:** Write clear, descriptive commit messages
  - Good: `Add health system with damage mechanics`
  - Bad: `fix stuff`
- **Code Style:** Keep it clean and readable
  - Add comments for complex logic
  - Use meaningful variable names
  - Follow PEP 8 conventions where possible
- **Testing:** Test your changes before submitting a PR
- **Pull Requests:** Include a brief description of what you added/changed

## Project Structure

```
learnpygame/
├── main.py              # Game entry point
├── requirements.txt     # Dependencies
├── README.md           # This file
└── [other project files]
```

## Current Features

- Player movement and controls
- Enemy AI and spawning
- Basic score tracking
- Game UI and display
- Game loop and collision detection

## Ideas for Your First Contribution

Not sure where to start? Try one of these:

1. **Add a pause menu** — Pressing 'P' pauses the game
2. **Implement sound effects** — Play audio when collecting items
3. **Add visual effects** — Screen shake on collision, particle explosions
4. **Create a difficulty selector** — Easy, Medium, Hard modes
5. **Improve the UI** — Better fonts, colors, layout
6. **Add documentation** — Improve code comments and docs

## Community

- **Questions?** Open a GitHub issue or discussion
- **Found a bug?** Report it with details on how to reproduce
- **Have an idea?** Suggest it in an issue before implementing

## Development Workflow

```bash
# Update your local main branch
git checkout main
git pull origin main

# Create your feature branch
git checkout -b feature/my-awesome-feature

# Make changes and commit
git add .
git commit -m "Add my awesome feature"

# Push to your fork and open a PR
git push origin feature/my-awesome-feature
```

## Before Submitting a PR

- [ ] Code runs without errors
- [ ] No breaking changes to existing features
- [ ] Comments added for new/complex code
- [ ] Commit messages are clear and descriptive
- [ ] You've tested the changes locally

## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python PEP 8 Style Guide](https://pep8.org/)
- [Git & GitHub Basics](https://guides.github.com/)

## License

This project is open source and available under the [MIT License](LICENSE).


**Ready to contribute?** Pick an issue, create a feature branch, and make this game awesome!