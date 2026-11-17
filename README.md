<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/grid-dark.svg">
  <img src="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/grid-light.svg" alt="yumuk.me written in a contribution grid" width="100%">
</picture>

<sub>Not my real contribution graph. Most of my work lives in private repositories.</sub>

### Hi, I'm Alper

Principal Software Engineer in Ankara, Türkiye. I build platforms as a developer: runtime frameworks, build tooling, and the Kubernetes platform they run on.

**What I work on**

- **Modernising a monolith.** Leading the strangler-fig modernisation of a .NET Framework 4.8 monolith running on around 600 Windows VMs. New microservices ship on the Linux-based Kubernetes platform we built (22 production AKS clusters, multi-tenant, 100% IaC) while the monolith is carved out step by step. Compute cost is down 40% so far.
- **A runtime standard.** A common .NET runtime framework (NuGet) and an umbrella Helm chart used by every service and team. Probes, PodDisruptionBudgets and priority classes come by default, so a lost node heals with no service impact.
- **Developer tooling.** An EF Core migrator where adding an object to a DbContext needs only a rebuild: a source generator prepares the DbContext, MSBuild tasks generate the migration-to-version map, and CI guardrails catch stale generated files.
- **AI-native engineering.** A personal meta-harness on Claude Code that surfaces one decision at a time, so the human stays in control. It lets me ship around 65 PRs a week.

**Stack:** C#, .NET, Azure, Kubernetes (AKS), Helm, GitOps, Istio, Gateway API, Crossplane, Terraform, Claude Code

**Elsewhere:** [yumuk.me](https://yumuk.me) (my resume as a vim buffer, try `:help`) · [LinkedIn](https://www.linkedin.com/in/alpercanyumuk/)
