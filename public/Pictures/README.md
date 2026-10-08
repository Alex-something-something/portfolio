# Portfolio picture and video guide

## Adding or replacing media

1. Put your file in the folder listed below, inside `public/Pictures`, with the exact filename and extension.
2. Refresh the page. Use Ctrl + F5 if a replaced image remains cached.
3. Missing media remains visible as an exact-filename placeholder. The placeholder is replaced automatically once the matching file loads.

Use real JPG, PNG and MP4 files matching the extensions. Renaming an extension does not convert the file. Match capitalization for future web hosting. Photos on cards are cropped to fit; PNG diagrams and detail-page images show the whole image. Videos start muted when enough of the video is visible and retain playback controls.

The headshot already exists. The same file can appear on a homepage card and its project page, so it only needs to be supplied once. The animated Argo blueprint and hero launch are drawn in code; they do not need picture files.

To change a slot later, edit its `data-media` path and `data-alt` description in the corresponding file under `content/`. Captions remain in those content files.

## Required filenames by folder

### Pictures

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Headshot.jpg | index.html | Portrait of Alexander Tong |

### Pictures/AIAA

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Prototype-1-Assembled.webp | index.html, dbf.html | Fully assembled Prototype 1 aircraft |
| Aircraft.jpg | dbf.html | Prototype 1 aircraft assembly CAD |
| Hot-Wire-Method.webp | dbf.html | Hot-wire cutting approach and airfoil templates |
| Prototype-1.png | dbf.html | Initial wing one-pager |
| Design-Review.png | dbf.html | Final design-review center-section CAD |
| Design-Review-Spar.png | dbf.html | Final design-review spar CAD |
| Design-Review-Servo.png | dbf.html | Final design-review servo-box CAD |
| Wing-Halves.jpg | dbf.html | Manufactured XPS wing halves |
| Wing-Fabrication.jpg | dbf.html | Prototype 1 wing assembly photo |
| Wing-Workbench.jpg | dbf.html | Wide wing-fabrication workbench photo |
| Prototype-2.png | dbf.html | Proposed Prototype 2 wing one-pager |
| Fiberglass-Layup.jpg | dbf.html | Fiberglass Layup Process Photo |
| Completed-Layup.jpg | dbf.html | Completed Fiberglass Layup Photo |

### Pictures/Aerocover

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Assembly.png | index.html, project_aerocover.html | Aerodynamic downcomer fairing CAD |
| Profile-Comparison.png | project_aerocover.html | Candidate Profile Comparison |
| Baseline-Comparison.png | project_aerocover.html | Icarus Baseline and Argo Concept |
| CFD.png | Reserved until results are approved | CFD visualization |
| FEA.png | Reserved until results are approved | Structural analysis |
| Carbon-Fiber-Thermal-Load-Test.jpg | project_aerocover.html | Curved carbon-fiber test article and heated static-load setup |

### Pictures/CO2

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Manufactured-Piercer-Card.webp | index.html | Centered CO₂ hardware thumbnail |
| Manufactured-Piercer.webp | project_co2.html | Manufactured CO₂ cartridge-piercing hardware |
| Piercer-Cross-Section-Vertical.webp | project_co2.html | Vertical piercer section with the CO₂ cartridge upward |
| First-Vacuum-Charge-Pressure.webp | project_co2.html, project_vacuum.html | First CO₂ charge pressure trace; co-lead instrumentation and analysis |
| ../Recovery/Vinyl-Charge-Nosecone-Test-Trimmed.mp4 | project_co2.html | Slow-motion black-powder deployment video used as failure context |

### Pictures/ME360

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Project.jpg | index.html | Course Project Photo |

### Pictures/Manufacturing

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Hammer.jpg | index.html, manufacturing.html | Machinist’s hammer made for BURPG MIP |

### Pictures/Nozzle

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Hotfire-Thumbnail.webp | index.html | Still frame from the nozzle hotfire video |
| Isometric.png | project_nozzle.html | Nozzle CAD image |
| Hotfire.mp4 | project_nozzle.html | Hotfire Test Slow Motion Video/GIF |
| Printed-Nozzle.jpg | project_nozzle.html | Fully resin-printed nozzle before hotfire |
| Mounting-Cross-Section.png | project_nozzle.html | Nozzle and mounting-adapter cross-section |
| Drawing.png | project_nozzle.html | SolidWorks Drawing |
| Rao-Angle-Reference.png | project_nozzle.html | Parabolic-nozzle angle reference chart |
| Bezier-Geometry.png | project_nozzle.html | CAD Bézier-curve geometry |
| Bezier-Points.png | project_nozzle.html | Published Rao parabolic-contour construction reference |
| FEA.png | project_nozzle.html | FEA Meshing Image |
| FEA-FOS.png | project_nozzle.html | Calculated yield FOS result |
| FEA-Von-Mises.png | project_nozzle.html | von Mises stress result |
| FEA-Fixturing.png | project_nozzle.html | Bolt-fixture boundary conditions |
| Pressure-Chamber.png | Archived; not displayed | Chamber-pressure load region |
| Pressure-Throat.png | Archived; not displayed | Throat-pressure load region |
| Pressure-External.png | Archived; not displayed | External and diverging-section pressure loads |
| Calculations.png | project_nozzle.html | Calculation Spreadsheet |

### Pictures/Plummer

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Lab-Overview.jpg | plummer.html | Dynamic-Test Fixture or Laboratory Photo |
| Shaker-Analysis.png | plummer.html | Shaker-Adapter CAD or FEA |
| Machined-Plate.jpg | plummer.html | Machined Plate Photo |
| Camera-Stand.jpg | plummer.html | Camera-Mount or Lab Buildout Photo |
| Lab-Fixtures.jpg | plummer.html | Laboratory Layout or Fixture Photo |

### Pictures/Culturon

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Published-Reactor-Schematic.png | culturon.html | Unmodified published analogue of a plasma-polymer nanoparticle reactor; not proprietary Culturon hardware |

### Pictures/Recovery

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| SepRec-CAD.webp | project_recovery.html | Nosecone assembly with hoist rings and CO₂ charges |
| SepRec-Top-Down.webp | index.html, project_recovery.html | Top-down packaging view with nosecone hidden |
| Vinyl-Charge-Nosecone-Test-Trimmed.mp4 | project_recovery.html | Slow-motion nosecone test with first eight seconds removed |
| Lines-Diagram.png | Source image retained for future editing | Full-resolution lines diagram |
| Lines-Diagram-Web.webp | project_recovery.html | Web-optimized System Architecture &amp; Lines Diagram |
| Connections.png | project_recovery.html | Simplified Connection Diagram |
| CDR-BP-Packing-Plan.webp | project_recovery.html | Earlier black-powder nosecone packing plan |
| Main-Parachute-Diagram.webp | project_recovery.html | Earlier main-parachute bag and line diagram |
| Pre-CO2-Coldflow-Setup.webp | project_recovery.html | Integrated hardware staged before CO₂ cold-flow operation |
| Cable-Cutter-Drawing.webp | project_recovery.html | Catclaw cable-cutter engineering drawing |
| Cable-Cutter-Assembly.webp | project_recovery.html | Manufactured Catclaw with zip tie in release slot |
| Cable-Cutter-Closeup.webp | project_recovery.html | Machined body and cord-path detail |
| Splice-Dynamic-Test.mp4 | project_recovery.html | Slow-motion dynamic recovery-line splice test |

### Pictures/Robot

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Vehicle.jpg | index.html, robot.html | Completed line-following car photograph |
| Front-CAD.jpg | robot.html | Front CAD view of the final vehicle |
| Chassis.png | robot.html | Internal chassis and electronics CAD |
| Rear-CAD.jpg | robot.html | Rear CAD showing switch and IR receiver |
| Sensors-And-Drive.jpg | robot.html | Motor, wheel, and IR sensor assembly |
| Remote-IR.jpg | robot.html | Soldered remote-control IR receiver |
| Course-Time.png | robot.html | Six course completion times |
| Course-Test.jpg | robot.html | Obstacle stopping distances |
| Battery-Test.png | robot.html | Battery voltage after two traversals |
| Wiring.png | robot.html | Final electrical wiring diagram |
| Course-Run.mp4 | robot.html | Silent course traversal video |
| Course-Run-Poster.jpg | robot.html | Video poster frame |

### Pictures/VEGAS

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Assembly.png | index.html | VEGAS fire-suppression assembly mounted to the test stand |

### Pictures/Vacuum

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Port-Valve-Side.webp | index.html, project_vacuum.html | Full chamber, port and valve side |
| Port-Detail.webp | project_vacuum.html | Port, gauge, and valve detail |
| Door-Removed.webp | project_vacuum.html | Door detached with black-powder residue visible |
| Door-Clamped.webp | project_vacuum.html | Door installed with mounting clamps |
| Chamber-Full.webp | project_vacuum.html | Full chamber from door side |
| ../CO2/First-Vacuum-Charge-Pressure.webp | project_vacuum.html | First CO₂ charge pressure trace; co-lead instrumentation and analysis |
| Door-CAD.png | project_vacuum.html | Vacuum-chamber door and tube-adapter CAD |
| Door calculation accordions | project_vacuum.html | Analytical plate sizing and seal review; no door FEA |

## Pages using code-drawn visuals

Culturon includes a published reference schematic plus NDA-safe code-drawn elevation and rack diagrams; Plummer includes sanitized code-drawn diagrams. APPT and COSSMo currently have text-only layouts. ME 360 has a homepage image slot; its detail page remains a course placeholder.

## Accessibility

Each loaded image has a descriptive text alternative. Update `data-alt` if your chosen image shows something different. Add captions or a transcript alongside a video if it includes meaningful speech or sound.
