---
title: WinUI 2.4 Release Notes
description: Release notes for WinUI 2.4 including new features and bug fixes.
ms.date: 05/04/2020
ms.topic: reference
---

# Windows UI Library 2.4

WinUI 2.4 is the latest official release of the Windows UI Library (WinUI).

WinUI is an open source project hosted on GitHub at [Windows UI Library repo](https://aka.ms/winui). Please register all bug reports, feature requests, and community code contributions in this repo.

WinUI Releases: [GitHub release page](https://github.com/microsoft/microsoft-ui-xaml/releases)

WinUI packages can be added to Visual Studio projects through the NuGet package manager. For more information, see [Getting Started with the Windows UI Library](../getting-started.md).

NuGet package download: [Microsoft.UI.Xaml](https://www.nuget.org/packages/Microsoft.UI.Xaml)

## New Features

### RadialGradientBrush fill style

A RadialGradientBrush is drawn within an ellipse defined by Center, RadiusX, and RadiusY properties. Colors for the gradient start at the center of the ellipse and end at the radius.

![Radial gradient brush](../images/radialgradientbrush.gif)<br>
*Radial gradient brush*

[Usage guidelines](/windows/uwp/design/style/brushes#radial-gradient-brushes)

[API reference](/uwp/api/microsoft.ui.xaml.media.radialgradientbrush)

### ProgressRing control

The ProgressRing control is used for modal interactions where the user is blocked until the ProgressRing disappears. Use this control if an operation requires that most interaction with the app be suspended until the operation is complete.

![ProgressRing control](../images/progressring.png)<br>
*ProgressRing control*

[Usage guidelines](/windows/uwp/design/controls-and-patterns/progress-controls)

[API reference](/uwp/api/microsoft.ui.xaml.controls.progressring)

[Sample link](/windows/uwp/design/controls-and-patterns/progress-controls#examples)

### TabView control updates

The TabView control updates provide you with more control over how to render tabs.

You can set the width of unselected tabs and show just an icon to save screen space:

![TabView control tab sizes](..\images\tabview-sizing.gif)<br>
*TabView control tab sizes*

You can also hide the close button on unselected tabs until the user hovers over the tab (in previous versions it was always shown):

![TabView control hover to close](..\images\tabview-closebuttononhover.gif)<br>
*TabView control hover to close*

[Usage guidelines](/windows/uwp/design/controls-and-patterns/tab-view)

[API reference](/uwp/api/microsoft.ui.xaml.controls.tabview)

### Dark theme updates for TextBox family controls

When dark theme is enabled, the background color of TextBox family controls remains dark by default on text insertion (in previous versions, the background color changes to light theme during text insertion).

The following are some of the controls included in the TextBox family of controls:

- [TextBox](/uwp/api/windows.ui.xaml.controls.textbox)
- [RichEditBox](/uwp/api/windows.ui.xaml.controls.richtextblock)
- [PasswordBox](/uwp/api/windows.ui.xaml.controls.passwordbox)
- [Editable ComboBox](/uwp/api/windows.ui.xaml.controls.combobox)
- [AutoSuggestBox](/uwp/api/windows.ui.xaml.controls.autosuggestbox)
