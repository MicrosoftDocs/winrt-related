---
title: UWP features not supported on Xbox
description: Xbox runs Windows 10, which means that it has the same core operating system as other devices in the Windows 10 family. But there are some feature areas that aren't at the same level of support on Xbox as they have on other devices.
ms.assetid: BAFF8085-8DDB-4DBA-AB3D-70DC92CD27AE
ms.topic: reference
ms.date: 09/02/2020
keywords: windows 10, uwp, xbox
---

# UWP features not supported on Xbox

Xbox runs Windows 10, which means that it has the same core operating system as other devices in the Windows 10 family&mdash;for example, desktop, IoT, and HoloLens. But there are some feature areas that aren't at the same level of support on Xbox as they have on other devices.

This topic lists some of the feature areas that your UWP app might use that don't function as fully on Xbox. All APIs are callable, and will fail gracefully if they're unsupported.

## Feature areas most applicable to Xbox

| Feature area | Details |
|-|-|
| Chat | [**Chat**](/uwp/api/Windows.ApplicationModel.Chat) APIs can create messages and add them to the database on Xbox but send/receive functionality is not supported.|
| Cortana voice commands | [**VoiceCommands**](/uwp/api/Windows.ApplicationModel.VoiceCommands) APIs are not supported on Xbox. |
| Credential APIs | APIs related to key credentials are not supported on Xbox. See [**Windows.Security.Credentials**](/uwp/api/Windows.Security.Credentials). |
| File system access | The [**broadFileSystemAccess**](/windows/uwp/files/file-access-permissions#accessing-additional-locations) capability is not supported on Xbox. |
| Kinect | Xbox Universal Windows Apps don't support skeletal tracking. Xbox provides support for using the infrared, depth, and color feeds from Kinect. |
| Launcher APIs | [**FolderLauncherOptions**](/uwp/api/Windows.System.FolderLauncherOptions) and [**LauncherUIOptions**](/uwp/api/Windows.System.LauncherUIOptions) APIs are not supported on Xbox. |
| Personalization | [**UserProfilePersonalizationSettings**](/uwp/api/Windows.System.UserProfile.UserProfilePersonalizationSettings) APIs are not supported on Xbox. |
| Photo import | [**Photo import**](/uwp/api/Windows.Media.Import) APIs are not supported on Xbox. |
| Share contract | [**Share**](/uwp/api/Windows.ApplicationModel.DataTransfer.ShareTarget) APIs are not supported on Xbox. No UI is displayed on calling share APIs. |
| Toast notifications | Toast notifications are partially supported on Xbox. Toasts fired on Xbox will show up to three lines of text and support an AppLogoOverride image on the toast. Action Center will also show the three lines of text, inline and hero images, attribution text, and up to five text actions (including input/picker actions). Unsupported features include: adaptive layouts (group/subgroup), context menu actions, action images, and custom sounds. See [**Windows.UI.Notifications**](/uwp/api/Windows.UI.Notifications). |
| Tile and badge notifications | Tile and badge notifications are not supported on Xbox. [**SecondaryTile**](/uwp/api/Windows.UI.StartScreen.SecondaryTile) is not supported on Xbox. See [**Windows.UI.Notifications**](/uwp/api/Windows.UI.Notifications).|
| Word breaker | Word breaker functionality is not supported on Xbox. |

## Feature areas less applicable to Xbox

| Feature area | Details |
|-|-|
| 3D printing | [**3D printing**](/uwp/api/windows.graphics.printing3d) is not supported on Xbox.|
| AllJoyn | [**AllJoyn**](/uwp/api/Windows.Devices.AllJoyn) APIs are not supported on Xbox. |
| App Capture | [**AppCapture**](/uwp/api/Windows.Media.Capture.AppCapture) APIs are not supported on Xbox. |
| Bluetooth | [**Bluetooth**](/uwp/api/Windows.Devices.Bluetooth) APIs are not supported on Xbox. |
| CachedFileUpdater | [**CachedFileUpdater**](/uwp/api/Windows.Storage.Provider.CachedFileUpdater) and [**CachedFileUpdaterUI**](/uwp/api/Windows.Storage.Provider.CachedFileUpdaterUI) are not supported on Xbox. |
| Casting | [**Casting**](/uwp/api/Windows.Media.Casting) and [**DialProtocol**](/uwp/api/Windows.Media.DialProtocol) APIs are not supported on Xbox. |
| Defining app settings on the settings page | [**AccountSettingsPane**](/uwp/api/Windows.UI.ApplicationSettings.AccountsSettingsPane) and [**WebAccountCommand**](/uwp/api/Windows.UI.ApplicationSettings.WebAccountCommand) APIs are not supported on Xbox. |
| Device Enumeration | Currently there is no [**DevicePicker**](/uwp/api/Windows.Devices.Enumeration.DevicePicker) UI on Xbox, so device enumeration APIs are not supported. |
| Drag and Drop | Drag and drop is not supported for Universal Windows Platform (UWP) apps on Xbox.See [**Windows.ApplicationModel.DataTransfer.DragDrop.Core**](/uwp/api/Windows.ApplicationModel.DataTransfer.DragDrop). |
| Folder picker scenarios | Scenarios related to folder pickers are not supported on Xbox. See [**FolderPicker**](/uwp/api/Windows.Storage.Pickers.FolderPicker) class. |
| Holographic APIs | [**Holographic**](/uwp/api/Windows.Graphics.Holographic) APIs are not supported on Xbox. |
| HumanInterfaceDevice Protocol APIs | [**HumanInterfaceDevice**](/uwp/api/Windows.Devices.HumanInterfaceDevice) APIs are not supported on Xbox. |
| Inking | [**Inking**](/uwp/api/Windows.UI.Input.Inking) APIs are not supported on Xbox. |
| LockScreen | The lock screen feature is not available on Xbox, so [**LockScreen**](/uwp/api/Windows.ApplicationModel.LockScreen) APIs are not supported. |
| Network Connectivity | [**NetworkUsage**](/uwp/api/Windows.Networking.Connectivity.NetworkUsage), [**ConnectivityInterval**](/uwp/api/Windows.Networking.Connectivity.ConnectivityInterval), [**NetworkInformation**](/uwp/api/Windows.Networking.Connectivity.NetworkInformation), and [**DataPlanStatus**](/uwp/api/Windows.Networking.Connectivity.DataPlanStatus) APIs are not supported on Xbox. |
| Network Operators API | APIs related to Network Operators require modem support, which is not present on Xbox. See [**Windows.Networking.NetworkOperators**](/uwp/api/Windows.Networking.NetworkOperators). |
| Near Field Communication (NFC) | [**NFC**](/uwp/api/Windows.Networking.Proximity) APIs are not supported on Xbox, so proximity APIs aren't supported. |
| Optical Character Recognition (OCR) | [**OCR**](/uwp/api/Windows.Media.Ocr) APIs are not supported on Xbox. |
| Printing | [**Printing**](/uwp/api/Windows.Graphics.Printing) is not supported on Xbox. |
| Point of Service (POS) | [**POS**](/uwp/api/Windows.Devices.PointOfService) APIs are not supported on Xbox. |
| Radios | [**Radio**](/uwp/api/Windows.Devices.Radios) APIs are not supported on Xbox |
| Roaming settings | [**Roaming settings**](/uwp/api/Windows.Storage.ApplicationData) are not synchronized on Xbox. The roaming setting APIs may be called, but settings will not be synchronized between devices. |
| Short Message Service (SMS) | [**SMS**](/uwp/api/Windows.Devices.Sms) APIs are not supported on Xbox. |
| VOIP | [**Windows.ApplicationModel.Calls**](/uwp/api/Windows.ApplicationModel.Calls) APIs are not supported on Xbox. |
| WiFi | [**Windows.Devices.Wifi**](/uwp/api/Windows.Devices.WiFi) APIs are not supported on Xbox. |
| WiFiDirect | [**WiFiDirect**](/uwp/api/Windows.Devices.WiFiDirect) APIs are not supported on Xbox. |
