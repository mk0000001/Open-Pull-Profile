# Development record — 2026-10-24

- User: printed tensile coupons for material/print-condition comparison; profile redesign based on CNC Kitchen; Ali/domestic sourcing with Coupang preference; publish an actual GitHub fork; maintain versions carefully.
- Baseline: original master 55017419fae89409b1098540212e1620b1e46d0b.
- Task1: design scope and provenance documented. Independent builder check found no planning blockers for the authorized concept stage.
- Task2 RED: native CAD validation failed with `Native FCStd has not been generated` before model generation.
- Task2 RED: first generated model failed the100mm pull collision check: crosshead bottom/rear intersected lower beams.
- Ruling: lengthen columns and screws from800 to900 and raise test/upper drive by100 — preserve100mm pull clearance — costs100mm additional overall height and slightly higher material cost.
- Task2 GREEN:58 part shapes valid; no moving-vs-frame/lower-bearing solid intersections at0/-100mm. Belt pitch length920mm at motor Y=-137.048851; proposed calibration640step/mm.
- Ruling: native CAD/source/envelopes are a design-review version, not machining drawings — vendor dimensions and hardware ratings unavailable — production fabrication still needs v0.2 interface work.
- Ruling: use AL6061-T6 as plate sourcing candidate and steel for grip adapters — manageable one-off weight and local availability — stiffness/strength and exact grade remain to be checked.
- Task3: sourcing differentiates product pages, search links, stale/indexed prices and unconfirmed options. No products ordered or supplier messages sent.
- Publishing: GitHub connector identifies mk0000001 but exposes no fork-creation tool; in-app GitHub browser is logged out. User login requested asynchronously while work continues. Upload remains pending until actual fork/authentication is available.
- Mechanical validation deferred: structural analysis, full hardware/mating tolerances, grip qualification, fall protection, electrical circuit, calibration and physical repeatability.
