---
title: uap:VoipCall
description: Declares an app extensibility point of type voipCall so that your app can declare that it can perform an upgrade from a cellular call to a VoIP video call, and/or whether it is a VoIP app that supports dialing phone numbers directly.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:VoipCall]
---

# uap:VoipCall

Declares an app extensibility point of type *voipCall* so that your app can declare that it can perform an upgrade from a cellular call to a VoIP video call, and/or whether it is a VoIP app that supports dialing phone numbers directly.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:VoipCall>`**  

## Syntax

```xml
<uap:VoipCall>

  <!-- Child elements -->
  uap:VoipCallUpgrade?
  uap:VoipDialPhoneNumber?

</uap:VoipCall>
```

### Key

`?` optional (zero or one)

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap:VoipCallUpgrade](element-uap-voipcallupgrade.md) | Indicates that the app supports video upgrade. Video upgrade is a feature on some mobile devices such that, when a user is on a cellular call, the user can upgrade that call to a VoIP video call if there is an app installed that can service such a request. |
| [uap:VoipDialPhoneNumber](element-uap-voipdialphonenumber.md) | Indicates that the app supports dialing phone numbers. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
