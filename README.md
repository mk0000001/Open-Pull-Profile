> **Current fork revision — v0.4.0-engineering-feasibility:** [UTM V2 / MT02 / room-temperature engineering study](profile/study-v0.4/README.ko.md), [updated quote excluding printing costs](profile/study-v0.4/QUOTE.ko.md). Recommended KRW589,084; reinforced planning allocation KRW789,084. Neither establishes a2kN rating, purchase-ready assembly or ISO conformance. Full-size10kN study is separate and exceeds this budget.

> **Frozen revision — v0.3.0-costdown-layout:** [Original-drive cost reduction and three saved FreeCAD frame variants](profile/build-v0.3/README.ko.md), [planning quote](profile/build-v0.3/SOURCING.ko.md), [NG-inspired printed frame comparison](profile/build-v0.3/PRINTED_FRAME.ko.md). A layout study: 2kN is a target, not an established rating. Planning cost exceeds KRW500,000; Ali seller authentication and final checkout remain unverified. The earlier KRW2.16million industrial subtotal was not the original CNC Kitchen BOM.

> **Frozen v0.2.0-interface-review:** [Domestic Korea sourcing and drawing-derived interfaces](profile/domestic-v0.2/README.ko.md). Original CNC Kitchen source directories remain preserved. [Frozen v0.1 tag](https://github.com/mk0000001/Open-Pull-Profile/releases/tag/v0.1.0-design), [provenance](UPSTREAM.md), [changes](CHANGELOG.md).

> **Earlier v0.1 concept:** [Build audit](profile/ASSEMBLY_AUDIT.ko.md). v0.2 corrects selected motor/screw/support/guide interfaces, removes unsupported M8 grip stems, and explicitly retains unresolved frame fastening, pulley torque transfer, sensing adapters and safety systems. Neither version is load-rated or ready for assembly.

__WORK IN PROGRESS__
# Open-Pull
These are all the files you need, to build your own DIY Universal test machine.

__SUPPORT__ my work via [PATREON](https://www.patreon.com/cnckitchen) or [PayPal](https://www.paypal.me/CNCKitchen).

Watch my YouTube video about it: https://youtu.be/uvn-J8CbtzM

__DISCLAIMER__: This is no professional test equipment! I won't be responsible for any damage that occured due to the data you gathered with this machine. Only use with appropriate safety equipment!
# Build one
## Hardware/CAD
CAD files of the whole assembly are available as stl, step and Fusion360 files.
### Bill of Materials (BOM)
* 2x NEMA 17 Stepper Motors 1.68A, Geared 14:1
* 2x Trapezoidal Lead Screw 10x2 500mm
* 2x Coupling 8/10mm
* 2x Trapezoidal Nut 10x2, Steel
* 2x Trapezoidal Nut with Flange, Brass
* 2x Angular Contact Bearing, 3200 2RS
* 2x Ball Bearing, 6202
* 4x Ball Bearing, 608
* ...

## Electronics
Currently the electronics are only as schematics and as images. I'd be happy if anyone made a PCB design for it for easier use.
### Bill of Materials (BOM)
* 1x Arduino Nano
* 2x A4988 Stepper Motor Driver
* 1x HX711 Load Cell Amplifier
* 1x 24V fan
* 1x 5A 24V Power Supply
* 1x Load Cell of suitable size (AEP TC4 - 5kN in my case)
* ...

## Software
Software is currently only the Arduino code for the machine itself, very rudamentary and not optimized. Everything is controlled via the serial terminal.

__UPDATE__: OpenPull Web-Controller(by Iqwertz): https://github.com/Iqwertz/OpenPull-Web-Controller

The general functionality is explained in this video: https://youtu.be/uvn-J8CbtzM
# Commands
* __M10__: Slow test (1mm/min)
* __M12__: Tare
* __M13__: Modulus test - 1mm/min for 30s, then 25mm/min
* __M14__: Fast test (25mm/min)
# Evaluation
The data is currently analyzed via [EXCEL sheets](Documents/DataAnalysis.xlsx).

The strain data is captures via an optical extensometer using a standard camera. I explain the procedure in my video, the tracking marker export script can be found in [Documents](Documents).

