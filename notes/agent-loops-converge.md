# Agent loops & converge (practical)

## One sentence

An **agent loop** repeats *think → act → observe* until a **real stop condition**, with a **max step limit**.

## Pseudocode

```python
for step in range(1, max_steps + 1):
    plan = model.think(history)
    if plan.done:
        break
    result = tools.run(plan.action)   # real world
    history.append(result)
else:
    raise RuntimeError("max steps")
```

## Converge vs claim

| Bad | Good |
|-----|------|
| Model says "video ready" | `review.mp4` exists and validates |
| Infinite retries | `max_attempts` + backoff |
| Memory only in chat | State in files / git |

## In our repos

- **Mind & Mythos** — converge until verified media; retrospective after publish
- **Polymath HQ** — `run_agent_loop` + PolicyEngine
- **RateBridge** — `converge()` for flaky rate fetches

## Superintelligence note

Research on *recursive self-improvement* is interesting. For production we only allow **gated** improvement (better state files, human PR), not unbounded self-rewriting.
