# Final resume and portfolio comparison — November 10, 2026

## Supplied final files

- PDF input: `Alex_s_Resume_11_10_26 (2).pdf`; copied without modification to `public/Resume/Alex_s_Resume.pdf`.
- Final LaTeX input: attachment `b0538fd5-44d8-4f0c-a278-b2028968bacb/Pasted text.txt`; copied without modification to `resume-drafts/Alexander_Tong_Space_Hardware.tex`.
- Active LaTeX content agrees with the one-page supplied PDF. Comments and text after `\end{document}` are source annotations, not active resume claims or instructions for this review.
- PDF SHA-256: `519fc1e6a67739b171ca0669c35800dc97933c03242b3f4329dd7cc91640a2d9`.
- LaTeX input SHA-256: `564120835b8ba44e187418ad0a6c251dbad2408a2793b1eeabc6f9ad216f2aa3`.

## Resolved questions and chosen portfolio wording

| Topic | Initial difference | Resolution from the author and supplied evidence |
| --- | --- | --- |
| Recovery sizing | Resume calls 1,230 lbf a snatch load; portfolio had described an applied 1.5 design FOS on 823 lbf | Supplied design-review slides distinguish opening shock from line-stretch/snatch shock and explicitly select approximately 1,230 lbf as a conservative snatch estimate. Use **823 lbf opening-load estimate / 1,230 lbf conservative snatch-load design estimate**. The historical Icarus event was tentatively estimated at 1,187 lbf, with unknown timing, torn drogue and restrained main; retain those limitations where the comparison is discussed. The slides establish the chosen design case, not an independently validated snatch prediction. |
| Splice trial | Estimated 1,800 lbf versus an earlier pending-audit description | Author explicitly chose **no observed slip at an estimated 1,800 lbf test load**. Retain the interval-average interpretation from momentum change/stopping time; peak force and ultimate strength remain unmeasured. Do not describe the estimated ratio as demonstrated proof strength or a measured gain over knots. |
| Instron result | Resume says verify coefficient; portfolio said coefficient not calculated | Author confirmed verification of the coefficient’s **sign and general behavior**, without determining its numerical magnitude. Update website and technical portfolio accordingly. |
| Bolt/adapter FOS | 2.46 minimum across named modes versus separate 1.49 bolt tensile-yield result | The named-mode minimum is consistent. Preserve 2.46 for bearing/thread-shear/pull-through checks and explain that bolt preload alone yields 1.50; the conservative preload-plus-full-external-load model yields 1.49. While clamped, only a fraction of an added separating load increases bolt tension. No joint-stiffness fraction has been calculated, so no revised numerical bolt ratio is claimed. |

Bolt mechanics reference: [NASA TM-106943, Preloaded Joint Analysis Methodology for Space Flight Systems](https://ntrs.nasa.gov/citations/19960012183), axial-load and joint-stiffness discussion. This explains the load-sharing model; it does not independently validate the installed joint.

The author controls resume wording; the supplied PDF and active LaTeX remain unchanged.

## Portfolio and technical-document updates

- Website dynamic-FEA bullet: specify the additional conservative 3 kg payload on top of the fixture and 0.44 mm relative deflection against a 1 mm limit.
- Technical portfolio: add the same dynamic case and highlight +40.7% calculated force-limited acceleration capacity (22.9 to 32.2 g) with a separate 0.50 kg scientific payload and the built-in 0.77 kg armature included.
- Replace stock-to-part framing with adapter-geometry optimization: 3.19 to 1.90 kg, 40.4% mass reduction through hand calculations and SolidWorks FEA.
- Add the same graph as a full-width standalone figure on technical-portfolio page 4; retain structural calculations, FEA and drawing evidence on page 5. Update the index and page totals to five. Keep the website graph as its existing standalone image. The 40.7% value applies to its force-limited plateau, not every frequency; the 3 kg structural case is distinct.
- Add the existing Culturon NDA limitation to its technical-portfolio summary and date the revised technical portfolio November 10, 2026.

## Consistent details requiring no factual changes

- Plummer intern title/dates; $71.11 versus $1,170 direct hardware cost; Haas VF-2; 6061-T6; stated machining tolerance.
- Culturon internship dates, sampling-rack work, four elevations, microscopy/ImageJ, proposed collection concepts and NDA notice. The website already contains NDA-limited descriptions and sanitized diagrams.
- Four-person fairing team, Mach 2.0–2.81 range, converged Mach 2.81 Ansys baseline still under review; proposed optimization remains pending in the detailed account.
- Argo dry mass and altitude target; complete 352 L chamber design; 1.1% atmospheric pressure; 1,663 lbf door load and 2.12 yield FOS; separate CO2 hoop FOS 2.01 and thread-shear FOS 6.31; SOP authorship and test leadership.
- Published approximately 2x splice-versus-knot comparisons remain selection rationale; they do not describe a personally measured strength improvement.
- AIAA complete-wing mass reduction 42.7% and three-to-one-month build time; nozzle 73% reduction, mechanical-load yield FOS 7.8 and approximately two-second hotfire.

## Small resume wording observations (not edited)

- “a ultraconservative” would normally be “an ultraconservative” (or simply “a conservative”).
- “48 Instron 68SC-5 testing” would normally be “48 Instron 68SC-5 tests.”
- “processed to verify coefficient” does not identify the processed data or coefficient; the portfolio now identifies the verified result as sign/general behavior, with no numerical magnitude.

## Verification and publication status

- Supplied resume inspected visually; one page, 19 bullets, selectable text, no replacement characters in pypdf/pdfplumber extraction.
- Updated technical portfolio rendered and inspected: five pages, with the graph on page 4 and structural evidence on page 5; complete footer/source links, no overflow. The project summary remains one page.
- Final website production build passed; all 16 static pages generated. Laptop (1366 px), mobile (390 px), and narrow-phone (320 px Plummer graph) checks passed; graph remains a standalone image.
- All factual questions resolved and files prepared for the requested GitHub publication. Commit and live-deployment results are reported in the chat.
