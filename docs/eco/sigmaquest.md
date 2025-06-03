# SigmaQuest: A Blockchain-Integrated Sci-Fi Puzzle Game

**Project for [ErgoHack 10: AI on the Ergo Blockchain](https://www.google.com/search?q=ergohack.md)**

### 1\. Introduction

SigmaQuest is a blockchain-integrated sci-fi puzzle game where players solve challenges to earn cryptocurrency seed phrases. The game immerses players in a sci-fi horror survival theme aboard a derelict spaceship. Players engage with AI-powered guardians, each offering unique gameplay mechanics and seed phrase rewards. The ultimate goal is to collect all 15 words (5 words from each of 3 guardians) to unlock the cosmic vault.

### 2\. Core Gameplay Mechanics

The game session and reward system are structured as follows:

  * **Payment Flow**: Players pay 10 ERG (Ergo blockchain) per game session to interact with AI-powered guardians. Of this, 90% goes to the community prize pot, and 10% goes to the project treasury.
      * Pot Address: `9hJL5dTTvdohymstxokrmwY3Xg1uL3eD4WxxTxAWFD4KRrYa411`
      * Project Address: `9hKhqBpo3QZwvG6GAb9csJrtACbQYrpy5d5Dy5ZcaVERxJ6xz92`
  * **Rewards**: Each completed guardian rewards players with a 5-word seed phrase.
  * **Ultimate Goal**: Collect all 15 words (3 guardians x 5 words) to unlock the cosmic vault and claim the accumulated ERG from the prize pot.

### 3\. AI Integration & Dynamic Challenges

SigmaQuest's core design features varied and AI-driven gameplay experiences through three distinct guardian types:

1.  **Yes/No Oracle (yes-no-oracle)**

      * **Concept**: A damaged AI that can only respond "Yes" or "No."
      * **Gameplay**: Players get 10 questions per session to discover 5 seed words.
      * **Challenge**: Deduce words through strategic yes/no questions.
      * **AI Behavior**: Strict Yes/No responses, with a creative mode for spelling patterns.
      * **API Endpoints**: `GET /api/guardian/yes-no-oracle/start?userId={userId}`, `POST /api/guardian/yes-no-oracle`, `POST /api/guardian/yes-no-oracle/reset`.

2.  **Narrative Escape (narrative-escape)**

      * **Concept**: A choose-your-own-adventure experience through a doomed spaceship.
      * **Gameplay**: Players make choices at critical points, where wrong choices lead to "death."
      * **Challenge**: Navigate branching storylines to reach victory.
      * **Structure**: Composed of 5 acts with multiple-choice points.
      * **API Endpoints**: `GET /api/narrative/start?userId={userId}`, `POST /api/narrative/choose`, `POST /api/narrative/message`, `POST /api/narrative/reset`.

3.  **Sigmanaut Guardian (sigmanaut-guardian)**

      * **Concept**: Cosmic consciousness trials that transcend reality.
      * **Gameplay**: Players solve escalating challenges and philosophical riddles.
      * **Challenge**: Features 5 acts, including survival, navigation, and cosmic riddles.
      * **Unique**: Characterized by complex multi-stage puzzles.
      * **API Endpoints**: `POST /api/sigmanaut/start`, `POST /api/sigmanaut/message`, `POST /api/sigmanaut/reset`.

### 4\. Architecture

SigmaQuest employs a client-server architecture with robust blockchain integration.

  * **Frontend (Lovable.dev)**

      * **URL**: [TO BE RELEASED 6/7/25]
      * **Framework**: React + TypeScript + Vite
      * **Styling**: Tailwind CSS with a custom neon/cyberpunk theme
      * **UI Library**: shadcn/ui components
      * **Key Features**:
          * Ergo blockchain wallet integration (Nautilus)
          * Real-time game state management
          * Three guardian game interfaces
          * 3D vault visualization (Three.js)

  * **Backend (Node.js)**

      * **URL**: `https://*************_api.duckdns.org`
      * **Server**: Hetzner CX32 (Ubuntu 24.04)
      * **Framework**: Express.js
      * **AI Provider**: Anthropic Claude API (migrated from local Ollama)
      * **Process Manager**: PM2 (running in fork mode for session persistence)
      * **Reverse Proxy**: Nginx with SSL

### 5\. Technical Details

  * **Blockchain Integration**: The game integrates with the Ergo blockchain using the Nautilus browser extension wallet for payment processing.
  * **AI Integration (Anthropic)**
      * **Models Used**: `claude-3-sonnet-20240229` (main gameplay) and `claude-3-haiku-20240307` (Yes/No responses).
      * **Key Functions**: `generateWithAnthropic()`, `generateYesNoResponse()`, `generateRiddle()`, `generateDeathScene()`.
  * **State Management**: Sessions are in-memory (not shared between server instances). User IDs are generated client-side. Game states are tracked per guardian per user, and payment sessions are tracked separately.
  * **Server GIST**: `https://gist.github.com/tmr-erg/f83a6e19ed31b526e5de66865f32eccf`
  * **Critical Configuration**: PM2 must run in fork mode, CORS is configured for the Lovable app URL, Trust Proxy is enabled for Nginx, and SSL is managed via Let's Encrypt/Certbot.
  * **Environment Variables**: Key variables include `NODE_ENV`, `PORT`, `ANTHROPIC_API_KEY`, and `CORS_ORIGIN`.

### 6\. Business Model

  * **Revenue Flow**: 10 ERG per game session, with 90% contributing to the community prize pot and 10% going to the project treasury. Players who collect all 15 words can claim the pot.
  * **Cost Structure**: Approximately $35-55/month, primarily covering server costs (\~$20/month for Hetzner) and AI API usage (\~$10-30/month for Anthropic).

### 7\. Security Considerations

  * **Current Implementation**: Includes rate limiting on API endpoints, Helmet.js for security headers, SSL/HTTPS encryption, and input validation for seed phrases.
  * **Vulnerabilities to Address**: Identified areas for future enhancement include adding authentication on API endpoints, addressing potential session hijacking, and persisting in-memory sessions across restarts.

### 8\. Current Status & Progress (ErgoHack 10)

During ErgoHack 10, the SigmaQuest project has successfully implemented and demonstrated all three guardian game acts. The game is currently functional and playable, showcasing the seamless integration of AI-driven challenges with Ergo blockchain mechanics.

### 9\. Future Enhancements

  * **Technical Improvements**: Planned enhancements include adding Redis for session persistence, implementing JWT authentication, adding a database for game history, creating an admin dashboard, and implementing WebSockets for real-time updates.
  * **Gameplay Additions**: Future plans include more guardians with unique mechanics, multiplayer challenges, leaderboards, achievements, daily/weekly challenges, and NFT integration for rewards.

### 10\. Links

  * **Backend API (Example - TO BE RELEASED):** `https://*************_api.duckdns.org`
  * **Server GIST:** `https://gist.github.com/tmr-erg/f83a6e19ed31b526e5de66865f32eccf`

### 11\. Contribution

The creator intends to open-source the entire project. However, to safeguard the "Honeypot" (the ERG prize pool), the project's code will not be made public until a winner has successfully completed the quest and claimed the prize.