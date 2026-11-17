<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/grid-dark.svg">
  <img src="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/grid-light.svg" alt="yumuk.me written in a contribution grid" width="100%">
</picture>

<sub>Not my real contribution graph. Most of my work lives in private repositories.</sub>

### Hi, I'm Alper

Principal Software Engineer in Ankara, Türkiye. I build platforms as a developer: runtime frameworks, build tooling, and the Kubernetes platform they run on.

**What I work on**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/stats-dark.svg">
  <img src="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/stats-light.svg" alt="600 Windows VMs under the monolith; 22 production AKS clusters; 40% lower compute cost so far; 65 PRs a week with Claude Code" width="100%">
</picture>

- **A monolith, carved out step by step.** A .NET Framework 4.8 system on around 600 Windows VMs, moving by strangler fig onto the Linux-based Kubernetes platform my team built: multi-tenant, 100% IaC. Still in progress, and compute cost is already down 40%.
- **One runtime for every service.** A common .NET runtime framework (NuGet) and an umbrella Helm chart that inject the cross-cutting concerns. Probes, PodDisruptionBudgets and priority classes are defaults, so a lost node heals with no service impact.
- **Tooling that removes steps.** An EF Core migrator: add an object to a DbContext, rebuild, done. A source generator and MSBuild tasks do the rest, and CI guardrails catch stale generated files.
- **AI-native engineering.** A meta-harness on Claude Code that surfaces one decision at a time, so the human stays in control. Around 65 PRs a week.

**Stack:** C#, .NET, Azure, Kubernetes (AKS), Helm, GitOps, Istio, Gateway API, Crossplane, Terraform, Claude Code

**Elsewhere:** [yumuk.me](https://yumuk.me) (my resume as a vim buffer, try `:help`) · [LinkedIn](https://www.linkedin.com/in/alpercanyumuk/)

<a href="https://yumuk.me">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/statusline-dark.svg">
    <img src="https://raw.githubusercontent.com/alpercanyumuk/alpercanyumuk/main/statusline-light.svg" alt="vim status line: type :help at yumuk.me" width="100%">
  </picture>
</a>
