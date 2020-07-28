---
title: UWP features not yet supported on Xbox
description: Xbox runs Windows 10, which means that it shares the same core operating system as other devices in the Windows 10 family desktop, mobile, and HoloLens.
ms.assetid: BAFF8085-8DDB-4DBA-AB3D-70DC92CD27AE
ms.topic: reference
ms.date: 07/28/2020
keywords: windows 10, uwp, xbox
---

# UWP features not yet supported on Xbox

Xbox runs Windows 10, which means that it has the same core operating system as other devices in the Windows 10 family: for example, desktop, IoT, and HoloLens. However, there are some feature areas that haven’t reached the same level of support on Xbox as they have on other devices.

This topic lists some of the feature areas that your UWP app might use that don’t currently function as fully on Xbox. All APIs are callable, and will fail gracefully if they’re unsupported.

## Feature areas most applicable to Xbox

| Feature area | Details |
|-|-|
| Chat | [**Chat**](https://msdn.microsoft.com/library/windows/apps/dn642321) APIs can create messages and add them to the database on Xbox but send/receive functionality is not supported.|
| Cortana voice commands | [**VoiceCommands**](https://msdn.microsoft.com/library/windows/apps/dn706594) APIs are currently not supported on Xbox. |
| Credential APIs | APIs related to key credentials are not supported on Xbox. See [**Windows.Security.Credentials**](https://msdn.microsoft.com/library/windows/apps/br227089). |
| File system access | The [**broadFileSystemAccess**](/windows/uwp/files/file-access-permissions#accessing-additional-locations) capability is not supported on Xbox. |
| Kinect | Xbox Universal Windows Apps don't support skeletal tracking. Xbox provides support for using the infrared, depth, and color feeds from Kinect. |
| Launcher APIs | [**FolderLauncherOptions**](https://msdn.microsoft.com/library/windows/apps/dn889612) and [**LauncherUIOptions**](https://msdn.microsoft.com/library/windows/apps/hh701448) APIs are not supported on Xbox. |
| Personalization | [**UserProfilePersonalizationSettings**](https://msdn.microsoft.com/library/windows/apps/mt244354) APIs are currently not supported on Xbox. |
| Photo import | [**Photo import**](https://msdn.microsoft.com/library/windows/apps/mt188534) APIs are currently not supported on Xbox. |
| Share contract | [**Share**](https://msdn.microsoft.com/library/windows/apps/br205989) APIs are not supported on Xbox. No UI is displayed on calling share APIs. |
| Toast notifications | Toast notifications are partially supported on Xbox. Toasts fired on Xbox will show up to three lines of text and support an AppLogoOverride image on the toast. Action Center will also show the three lines of text, inline and hero images, attribution text, and up to five text actions (including input/picker actions). Unsupported features include: adaptive layouts (group/subgroup), context menu actions, action images, and custom sounds. See [**Windows.UI.Notifications**](https://msdn.microsoft.com/library/windows/apps/br208661). |
| Tile and badge notifications | Tile and badge notifications are not supported on Xbox. [**SecondaryTile**](https://msdn.microsoft.com/library/windows/apps/br242183) is not supported on Xbox. See [**Windows.UI.Notifications**](https://msdn.microsoft.com/library/windows/apps/br208661).|
| Word breaker | Word breaker functionality is not supported on Xbox. |

## Feature areas less applicable to Xbox

| Feature area | Details |
|-|-|
| 3D printing | [**3D printing**](https://msdn.microsoft.com/library/windows/apps/dn706164) is not supported on Xbox.|
| AllJoyn | [**AllJoyn**](https://msdn.microsoft.com/library/windows/apps/dn894971) APIs are not supported on Xbox. |
| App Capture | [**AppCapture**](https://msdn.microsoft.com/library/windows/apps/mt608892) APIs are not supported on Xbox. |
| Bluetooth | [**Bluetooth**](https://msdn.microsoft.com/library/windows/apps/dn263413) APIs are not supported on Xbox. |
| CachedFileUpdater | [**CachedFileUpdater**](https://msdn.microsoft.com/library/windows/apps/hh747793) and [**CachedFileUpdaterUI**](https://msdn.microsoft.com/library/windows/apps/hh747794) are not supported on Xbox. |
| Casting | [**Casting**](https://msdn.microsoft.com/library/windows/apps/dn972568) and [**DialProtocol**](https://msdn.microsoft.com/library/windows/apps/dn946818) APIs are not supported on Xbox. |
| Defining app settings on the settings page | [**AccountSettingsPane**](https://msdn.microsoft.com/library/windows/apps/dn298377) and [**WebAccountCommand**](https://msdn.microsoft.com/library/windows/apps/dn298413) APIs are not supported on Xbox. |
| Device Enumeration | Currently there is no [**DevicePicker**](https://msdn.microsoft.com/library/windows/apps/dn930841) UI on Xbox, so device enumeration APIs are not supported. |
| Drag and Drop | Drag and drop is not supported for Universal Windows Platform (UWP) apps on Xbox.See [**Windows.ApplicationModel.DataTransfer.DragDrop.Core**](https://msdn.microsoft.com/library/windows/apps/dn894216). |
| Folder picker scenarios | Scenarios related to folder pickers are currently not supported on Xbox. See [**FolderPicker**](https://msdn.microsoft.com/library/windows/apps/br207881) class. |
| Holographic APIs | [**Holographic**](https://msdn.microsoft.com/library/windows/apps/mt592853) APIs are not supported on Xbox. |
| HumanInterfaceDevice Protocol APIs | [**HumanInterfaceDevice**](https://msdn.microsoft.com/library/windows/apps/dn264174) APIs are not supported on Xbox. |
| Inking | [**Inking**](https://msdn.microsoft.com/library/windows/apps/br208524) APIs are not supported on Xbox. |
| LockScreen | The lock screen feature is not available on Xbox, so [**LockScreen**](https://msdn.microsoft.com/library/windows/apps/dn946802) APIs are not supported. |
| Network Connectivity | [**NetworkUsage**](https://msdn.microsoft.com/library/windows/apps/dn303657), [**ConnectivityInterval**](https://msdn.microsoft.com/library/windows/apps/dn266097), [**NetworkInformation**](https://msdn.microsoft.com/library/windows/apps/br207293), and [**DataPlanStatus**](https://msdn.microsoft.com/library/windows/apps/br207256) APIs are not supported on Xbox. |
| Network Operators API | APIs related to Network Operators require modem support, which is not present on Xbox. See [**Windows.Networking.NetworkOperators**](https://msdn.microsoft.com/library/windows/apps/br241148). |
| Near Field Communication (NFC) | [**NFC**](https://msdn.microsoft.com/library/windows/apps/br241250) APIs are not supported on Xbox, so proximity APIs aren't supported. |
| Optical Character Recognition (OCR) | [**OCR**](https://msdn.microsoft.com/library/windows/apps/dn974149) APIs are not supported on Xbox. |
| Printing | [**Printing**](https://msdn.microsoft.com/library/windows/apps/br226489) is currently not supported on Xbox. |
| Point of Service (POS) | [**POS**](https://msdn.microsoft.com/library/windows/apps/dn298071) APIs are not supported on Xbox. |
| Radios | [**Radio**](https://msdn.microsoft.com/library/windows/apps/dn996447) APIs are not supported on Xbox |
| Roaming settings | [**Roaming settings**](https://msdn.microsoft.com/library/windows/apps/br241624) are not synchronized on Xbox. The roaming setting APIs may be called, but settings will not be synchronized between devices. |
| Short Message Service (SMS) | [**SMS**](https://msdn.microsoft.com/library/windows/apps/br206567) APIs are not supported on Xbox. |
| VOIP | [**Windows.ApplicationModel.Calls**](https://msdn.microsoft.com/library/windows/apps/dn297266) APIs are not supported on Xbox. |
| WiFi | [**Windows.Devices.Wifi**](https://msdn.microsoft.com/library/windows/apps/dn975224) APIs are not supported on Xbox. |
| WiFiDirect | [**WiFiDirect**](https://msdn.microsoft.com/library/windows/apps/dn297687) APIs are not supported on Xbox. |
