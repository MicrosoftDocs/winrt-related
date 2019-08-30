---
title: WinUI 2.2 Release Notes
description: Release notes for WinUI 2.2 including new features and bugfixes.
author: predavid
ms.author: mijacobs
ms.date: 04/16/2019
ms.topic: reference
---

# Windows UI Library 2.2

WinUI 2.2 is the latest official release of the Windows UI Library. 

You can add WinUI packages to your app using the NuGet package manager: see [Getting Started with the Windows UI Library](../getting-started.md) for more information.

WinUI is an open source project hosted on GitHub. We welcome bug reports, feature requests and community code contributions in the [Windows UI Library repo](https://aka.ms/winui).

## Microsoft.UI.Xaml 2.2 Version History

### Windows UI Library 2.2 Official Release

AUGUST 2019

[GitHub release page](https://github.com/microsoft/microsoft-ui-xaml/releases/tag/v2.2.190702001-prerelease)

[NuGet package download](https://www.nuget.org/packages/Microsoft.UI.Xaml/2.2.190702001-prerelease)

### New Features

#### 1) TabView

![Example](../images/TabView%20GIF.gif)

#### Description: 
The TabView control is a collection of tabs that each represents a new page or document in your app. TabView is useful when your app has several pages of content and the user expects to be able to add, close, and rearrange the tabs. The new [Windows Terminal](https://github.com/Microsoft/Terminal) uses TabView to show multiple command line interfaces. 

#### MSDN Doc Link:  
https://docs.microsoft.com/en-us/uwp/api/microsoft.ui.xaml.controls.tabview?view=winui-2.2

#### 2) NavigationView Updates

#### a) NavigationView's Back Button update

![Example](../images/NavigationView_BackButton.gif)

#### Description: 
In NavigationView’s minimal mode, the back button no longer disappears. When opening and closing the pane, users no longer need to move their cursor to click the hamburger button. This feature will work by default. You don't need to make any code changes to make this work.

#### b) NavigationView - No Auto Padding

![Example](../images/NavigationView_NoAutoPadding.png)

#### Description: 
App developers can now reclaim all pixels within their app window when they use the NavigationView control and extend into the title bar area.

#### MSDN Doc Link:  
https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/navigationview#top-whitespace

#### 3) Santorini Style Updates

#### a) Corner Radius Update

![Example](../images/CornerRadius.png)

#### Description: 
CornerRadius attribute was added. Default controls were updated to use slightly rounded corners. Developers can easily customize the corner radius to give your app a unique look if desired.

#### GitHub Spec Link:  
https://github.com/microsoft/microsoft-ui-xaml/issues/524

#### b) Border Thickness Update

![Example](../images/BorderThickness.png)

#### Description: 
BorderThickness property was made easier to customize. Default controls were updated to reduce the outlines to be thinner for a cleaner and familiar look.

#### GitHub Spec Link:  
https://github.com/microsoft/microsoft-ui-xaml/issues/835

#### c) Button Visual Update

![Example](../images/ButtonHoverVisualUpdate.png)

#### Description: 
Default Button’s visual was updated to remove outline that appeared during hover to give it a cleaner look.

#### GitHub Spec Link:  
https://github.com/microsoft/microsoft-ui-xaml/issues/953

#### d) SplitButton Visual Update

![Example](../images/SplitButtonVisualUpdate.png)

#### Description: 
Default SplitButton’s visual was updated to make it more distinct from DropDownButton.

#### GitHub Spec Link: 
https://github.com/microsoft/microsoft-ui-xaml/issues/986

#### e) ToggleSwitch Visual Update

![Example](../images/ToggleSwitchUpdate.png)

#### Description: 
Default ToggleSwitch’s width was reduced from 44px to 40px so it is balanced visually while retaining usability.

#### GitHub Spec Link: 
https://github.com/microsoft/microsoft-ui-xaml/issues/836


### Microsoft.UI.Xaml 2.2.190702001-prerelease

July 2019

[GitHub release page](https://github.com/microsoft/microsoft-ui-xaml/releases/tag/v2.2.190702001-prerelease)

[NuGet package download](https://www.nuget.org/packages/Microsoft.UI.Xaml/2.2.190702001-prerelease)

### Experimental Feature

* [TabView](https://docs.microsoft.com/en-us/uwp/api/microsoft.ui.xaml.controls.tabview?view=winui-2.2)

### Microsoft.UI.Xaml 2.2.20190416001-prerelease

April 2019

[GitHub release page](https://github.com/Microsoft/microsoft-ui-xaml/releases/tag/v2.2.190416008-prerelease)

[NuGet package download](https://www.nuget.org/packages/Microsoft.UI.Xaml/2.2.190416008-prerelease)

#### Experimental features

* [FlowLayout](https://docs.microsoft.com/uwp/api/microsoft.ui.xaml.controls.flowlayout)

* [LayoutPanel](https://docs.microsoft.com/uwp/api/microsoft.ui.xaml.controls.layoutpanel)

* [RadioButtons](https://docs.microsoft.com/uwp/api/microsoft.ui.xaml.controls.radiobuttons)

* [ScrollViewer](https://docs.microsoft.com/uwp/api/microsoft.ui.xaml.controls.scrollviewer)
