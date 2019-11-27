---
title: WinUI 2.3 Release Notes
description: Release notes for WinUI 2.3 including new features and bug fixes.
author: Karl-Bridge-Microsoft
ms.author: kbridge
ms.date: 11/22/2019
ms.topic: reference
---

# Windows UI Library 2.3

WinUI 2.3 is the latest official release of the Windows UI Library.

You can add WinUI packages to your app using the NuGet package manager: see [Getting Started with the Windows UI Library](../getting-started.md) for more information.

WinUI is an open source project hosted on GitHub. We welcome bug reports, feature requests and community code contributions in the [Windows UI Library repo](https://aka.ms/winui).

[GitHub release page](https://github.com/microsoft/microsoft-ui-xaml/releases)

[NuGet package download](https://www.nuget.org/packages/Microsoft.UI.Xaml)

## New Features 

### 1) Progress Bar Visual Refresh

#### Indeterminate Progress Bar 

![Example](../images/IndeterminateProgressBar.gif)

#### Determinate Progress Bar

![Example](../images/IndeterminateProgressBar.gif)

#### Description: 
The ProgressBar has two differnt visual represetations. 
Indeterminate - shows that a task is ongoing , but dosen't block user interaction. 
Determinate - shows how much progress has been made on a known amount of work. 

[Doc link](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/progress-controls) 

[Sample Link](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/progress-controls#examples)


### 2) Radio Buttons

![Example](../images/RadioButtons.png)

#### Description 
RadioButtons is a new container control that enables you to create related groups of RadioButton elements easily, while also correctly supporting keyboarding and narrator/screen reader functionality

[Doc and Sample Link](https://github.com/microsoft/microsoft-ui-xaml-specs/blob/c8d3d3668af546091656dfc37436b13cd062f52d/active/radiobuttons/RadioButtons_Spec.md)


### 3) NumberBox

![Example]

#### Description 
NumberBox represents a control that can be used to display and edit numbers. This supports validation, increment stepping, and computing inline calculations of basic equations, such as multiplication, division, addition, and subtraction.

[Doc and Sample Link](https://github.com/microsoft/microsoft-ui-xaml-specs/blob/e016c9baa154d76ba3f61d2692af97fe6c0613b6/active/NumberBox/NumberBox.md)



