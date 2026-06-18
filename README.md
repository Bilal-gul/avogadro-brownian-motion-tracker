# 🔬 Autonomous Brownian Motion Analyzer & Avogadro Constant Calculator

An advanced computer vision pipeline engineered to autonomously track the chaotic trajectories of microscopic pollen particles (Brownian Motion) and mathematically compute the **Avogadro Constant** utilizing the Einstein-Stokes Diffusion Theory.

---

## 🚀 Core Engineering & Computer Vision Solutions

* **Overlapping Particle Segmentation:** Implements a strict `cv2.distanceTransform` and watershed-based core isolation routine to prevent ID swapping and particle merging during physical contact.
* **Dynamic Centroid Tracking:** Computes instantaneous center-of-mass matrices via `cv2.moments`, executing deterministic trajectory assignments across successive frames using spatial Euclidean distance minimization.
* **Macro-Physical Calibration:** Maps pixel space coordinates to international metric standards (`PIXEL_TO_METER`) via manual spatial calibration, converting raw digital coordinates into high-precision kinematic datasets.

---

## 📊 Analytical Performance Metrics

Based on the statistical analysis of 9,006 sequential displacement vectors, the analytical pipeline converged with remarkable precision against reference physical boundaries:

| Kinematic / Physical Parameter | Empirical Computed Value |
| :--- | :--- |
| **Total Processed Displacement Vectors** | 9,006 Data Points |
| **Computed Diffusion Coefficient ($D$)** | $1.4309 \times 10^{-13} \text{ m}^2/\text{s}$ |
| **Empirically Calculated Avogadro Constant ($N_A$)** | **$6.0244 \times 10^{23}$** |
| **Theoretical Standard Value** | **$6.022 \times 10^{23}$** |
| **Experimental Margin of Error** | **%0.04** |

---

## 🛠️ Stack & Dependency Layer
* **Python 3** - Primary execution runtime.
* **OpenCV** - Real-time matrix manipulation and computer vision algorithms.
* **NumPy** - Vectorized linear algebra and kinematic tensor computations.

---

## 📌 Acknowledgment & Data Sources
The high-resolution microscopic pollen trajectory videos utilized for pipeline validation were sourced from public educational content repositories on YouTube. In alignment with academic integrity and data citation standards, the source components have been fully referenced and structured within this repository.
