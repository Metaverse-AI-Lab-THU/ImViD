<div align="center">

# ImViD: Immersive Volumetric Videos for Enhanced VR Engagement

<h2 align="center">
  🌟 CVPR 2025 Highlight 🌟
</h2>
 
<h2 align="center">
  <img src="assets/tsinghua.png" alt="Tsinghua" width="24" /> 
  <strong><a href="https://www.tsinghua.edu.cn/">Tsinghua University</a></strong> &nbsp;&nbsp;
  <br>
  <img src="assets/migu.png" alt="Migu" width="24" /> 
  <strong><a href="https://www.migu.cn/">Migu Beijing Research Institute</a></strong> &nbsp;&nbsp;
  <img src="assets/casia.jpg" alt="CASIA" width="24" /> 
  <strong><a href="http://www.ia.cas.cn/">IACAS</a></strong>
</h2>

[Zhengxian Yang]()\*,[Shi Pan]()\*, [Shengqi Wang]()*, [Haoxiang Wang](), [Li Lin](), [Guanjun Li](),

[Zhengqi Wen]()†, [Borong Lin](https://www.arch.tsinghua.edu.cn/info/Building%20Science%20and%20Technology/1804)†, [Jianhua Tao](https://www.au.tsinghua.edu.cn/info/1104/2986.htm)†, [Tao Yu](https://ytrock.com/)†,

<p align="center"><small>  
* Equal Contribution,  
† Corresponding Authors  
</small></p>

[![paper](https://img.shields.io/badge/CVPR‑2025‑OpenAccess-brightgreen.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_ImViD_Immersive_Volumetric_Videos_for_Enhanced_VR_Engagement_CVPR_2025_paper.html)
[![arXiv](https://img.shields.io/badge/arXiv-2503.14359-orange.svg)](https://arxiv.org/abs/2503.14359)
[![Project](https://img.shields.io/badge/Project-Page-blue.svg)](https://yzxqh.github.io/ImViD/)
[![YouTube](https://img.shields.io/badge/YouTube-Video-red?logo=youtube)](https://www.youtube.com/watch?v=qRl8lEAIPGI)

<p align="center">
  <a href="https://www.qbitai.com/2025/06/293352.html">
    <img src="https://img.shields.io/badge/量子位-深度解读-orange?style=flat-square" alt="量子位"/>
  </a>
  <a href="https://mp.weixin.qq.com/s/Pq-4varyObluQDlO2wdZdg">
    <img src="https://img.shields.io/badge/VR陀螺-微信公众号-green?logo=wechat&style=flat-square" alt="VR陀螺"/>
  </a>
  <a href="https://mp.weixin.qq.com/s/h37fSyYOfsucUrt1bIytHA">
    <img src="https://img.shields.io/badge/3D视觉之心-微信公众号-blue?logo=wechat&style=flat-square" alt="3D视觉之心"/>
  </a>
</p>
</div>

---

## Overview
<p align="center">
  <img src="assets/trailercollage2.jpg" alt="ImViD Teaser" width="90%" />
</p>

We introduce **ImViD**, a multi-view, multi-modal dataset featuring complete space-oriented data capture and various indoor/outdoor scenarios. The dataset includes high-resolution, synchronized audiovisual content captured at 5K resolution and 60 frames per second, with durations ranging from 1 to 5 minutes.

## Download
The full dataset has been released. To obtain access:

1. Download and fill the application forms: 
   - Fillable PDF: [docs/application_form.pdf](docs/application_form.pdf)
2. Email the completed form to the contacts listed in the Contact section below.
3. Upon approval, we will send you the download instructions.

For a quick look, a small sample dataset is available on the [Release Page](https://github.com/Metaverse-AI-Lab-THU/ImViD/releases/tag/v0.2). The sample includes Scene 1 videos (300×5K@60 FPS, H.264 MP4) and COLMAP-style camera metadata files: `cameras.txt` and `images.txt`.

## Dataset Summary

| Scene      | Cameras | Static VPs | Takes | Strategy   | Avg. S-T Density (m³/s) | Viewing Space | Duration | Storage (GB) |
| :--------- | :-------:| :---------: | :----: | :---------: | :-----------------------: | :-----------: | :-------: | :----------: |
| Opera     | 39      | 1152      | 2     | 1–180°     | –                       | 180°          | 3:22     | 226         |
| Laboratory | 39      | 1225      | 2     | 2          | 0.10                    | 360°          | 1:42     | 137.3       |
| Classroom  | 39      | 1223      | 2     | 2          | 0.10                    | 360°          | 4:42     | 497         |
| Meeting    | 39      | 1223      | 1     | 1–360°     | –                       | 360°          | 3:16     | 114         |
| Rendition  | 39      | 1620      | 4     | 2          | 0.10                    | 360°          | 2:02     | 516         |
| Puppy      | 39      | 1404      | 3     | 2          | 0.10                    | 360°          | 1:50     | 359         |
| Playing    | 39      | 1224      | 2     | 2          | 0.10                    | 360°          | 1:10     | 220         |
| **Total**  | –       | –         | 16    | –          | –                       | –             | 38:46    | 2069.3      |

## Preview Clips

Below are low-bitrate preview clips for each scene.

<table align="center">
  <tr>
    <td align="center">
      <img
        src="assets/scene1.gif"
        alt="Scene 1: Opera Preview"/><br/>
      Scene 1: Opera
    </td>
    <td align="center">
      <img
        src="assets/scene2.gif"
        alt="Scene 2: Laboratory Preview"/><br/>
      Scene 2: Laboratory
    </td>
    <td align="center">
      <img
        src="assets/scene3.gif"
        alt="Scene 3: Classroom Preview"/><br/>
      Scene 3: Classroom
    </td>
  <tr>
  <tr>
    <td align="center">
      <img
        src="assets/scene4.gif"
        alt="Scene 4: Meeting Preview"/><br/>
      Scene 4: Meeting
    </td>
    <td align="center">
      <img
        src="assets/scene5.gif"
        alt="Scene 5: Rendition Preview"/><br/>
      Scene 5: Rendition
    </td>
    <td align="center">
      <img
        src="assets/scene6.gif"
        alt="Scene 6: Puppy Preview"/><br/>
      Scene 6: Puppy
    </td>
  </tr>
  <tr>
    <td align="center" colspan="3">
      <img
        src="assets/scene7.gif"
        alt="Scene 7: Playing Preview"/><br/>
      Scene 7: Playing
    </td>
  </tr>
</table>

## Using the Dataset

### Extracting Frames

To extract individual frames from the sample video:
```bash
python scripts/extract_frames.py \
    --input path/to/your_video_folder \
    --output path/to/output_frames_folder \
```

### Camera Parameters

The `cameras.txt` and `images.txt` follow COLMAP’s native format. You can feed them directly into COLMAP and run `point_triangulator` tool to obtain an SfM point cloud.

> **Note:** Make sure the frame filenames exactly match the image names listed in `images.txt`. You can either update `images.txt` or rename the extracted images to correspond to the entries in `images.txt`.

## Moving Rig Captured Data

We also provide the captured data with the moving rig. This data poses significant challenges for existing calibration methods, often resulting in errors and floaters. But we believe that this data will greatly contribute to the advancement of the field, and thus we also publicly releasing the data. For more details, refer to our [paper](https://arxiv.org/abs/2503.14359).

## TODO
- [x] Release the sample dataset and download instructions.
- [x] Release the full dataset.
- [ ] Release the calibration code for the moving rig captured data.

> 🎉 Stay tuned for our upcoming work: an enhanced 4D Gaussian Splatting method for volumetric video.

## Citation
```bibtex
@InProceedings{Yang_2025_CVPR,
    author    = {Yang, Zhengxian and Pan, Shi and Wang, Shengqi and Wang, Haoxiang and Lin, Li and Li, Guanjun and Wen, Zhengqi and Lin, Borong and Tao, Jianhua and Yu, Tao},
    title     = {ImViD: Immersive Volumetric Videos for Enhanced VR Engagement},
    booktitle = {Proceedings of the Computer Vision and Pattern Recognition Conference (CVPR)},
    month     = {June},
    year      = {2025},
    pages     = {16554-16564}
}
```

## Contact

For access to the full dataset, please contact:
- **Zhengxian Yang**: zx-yang23@mails.tsinghua.edu.cn
- **Shengqi Wang**: shengqi-21@mails.tsinghua.edu.cn

## License
This project is licensed under the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. You are free to share and adapt the material, provided you give appropriate credit, indicate if changes were made, and do not apply legal terms or technological measures that restrict others from using the material.
