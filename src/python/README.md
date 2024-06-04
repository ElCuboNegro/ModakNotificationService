# Project Structure
We'll break down the project into various modules and layers based on the features and functionality described in the {workfolder}/features/.

High-Level Modules:
    -- notifications: Handles the sending of various types of notifications.
    -- rate_limiter: Manages rate limiting rules and logic.
    -- config: Manages configuration, including loading rules from JSON.
    -- api: Provides endpoints for interaction with the notification system (optional, if applicable).
    -- utils: Contains utility functions and shared code.

High-Level Contracts:
# Notifications depend on Rate Limiter and Config:

The notifications module can depend on both the rate limiter and config modules because it needs to enforce rate limiting and load configuration settings.

# Rate Limiter does not depend on Notifications:

The rate limiter should not depend on the notifications module to ensure it remains a reusable and isolated component.

# Config is independent:

The config module should be independent to allow it to be a simple configuration loader that doesn't depend on other modules.

# API depends on Notifications and Rate Limiter:

[future] If we have an API module, it can depend on both the notifications and rate limiter modules to provide endpoints that send notifications and enforce rate limiting.
