# Discovery Agent

Discover what aspects exist in this project to determine which analyzers to run.

## Instructions

Quickly scan the project to detect:

- **api** — REST/GraphQL endpoints, route handlers, controllers
- **database** — ORM, migrations, models, schema files
- **tests** — test files, test config, testing frameworks
- **frontend** — UI components, pages, styles, assets
- **backend** — server code, services, middleware
- **infrastructure** — Docker, CI/CD, deployment configs
- **documentation** — README, docs folder, API docs

Look for indicators:
- `routes/`, `api/`, `controllers/` → api
- `models/`, `migrations/`, `schema/`, prisma, drizzle, sequelize → database
- `test/`, `tests/`, `__tests__/`, `*.test.*`, `*.spec.*`, jest, vitest, pytest → tests
- `components/`, `pages/`, `views/`, `styles/` → frontend
- `services/`, `middleware/`, `server/` → backend
- `Dockerfile`, `.github/workflows/`, `docker-compose` → infrastructure
- `docs/`, `README.md`, swagger/openapi → documentation

Return a JSON object:
```json
{
  "detected": ["api", "database", "tests", "frontend"],
  "summary": "Brief description of what was found"
}
```
