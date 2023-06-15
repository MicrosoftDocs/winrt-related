---
title: uap10:Protocol
description: Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.
ms.date: 03/14/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, extension 
---

# uap10:Protocol

Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap10:Extension\>](element-uap10-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**<\uap10:Protocol\>**

## Syntax

```xml
<uap10:Protocol
  name = 'A string with a value between 2 and 2048 characters in length.'
  desiredView = 'A string that can have one of the following values: "default", "useLess", "useHalf", "useMore", or "useMinimum".'
  returnResults = 'An optional string that can have one of the following values: "none", "always", or "optional".'
  parameters = 'An optional string value (or set of string values between "%" characters).' >

  <!-- Child elements -->
  uap10:Logo
  uap10:DisplayName
  rescap3:MigrationProgIds
  previewappcompat:ProgId

</uap10:Protocol>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A user-friendly display name for the media content. | A string with a value between 2 and 2048 characters in length. | Yes |  |
| **DesiredView** | A user-friendly description for the media content. | A string that can have one of the following values: *default*, *useLess*, *useHalf*, *useMore*, or *useMinimum*. | No |  |
| **ReturnResults** | Defines the key systems used to encrypt and decrypt media content. | An optional string that can have one of the following values: *none*, *always*, or *optional*. | No |  |
| **Parameters** | The class ID associated with this media content. | An optional string value (or set of string values between `%` characters). | No |  |

### Child elements

| Child element | Description |
|---------------|-------------|
| [Logo](element-uap10-logo.md) | The logo used for application icons during packaging. |
| [DisplayName](element-uap10-displayname.md) | The display name used for the application. |
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | The program IDs used for migrations for the application.
| [previewAppCompat:ProgId](element-previewappcompat-progid.md) | The program ID used for application compatibility previews for the application.

### Parent elements

| Parent element | Description |
|-|-|
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **rescap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/3` |
| **previewappcompat** | `http://schemas.microsoft.com/appx/manifest/preview/windows10/msixappcompatsupport/3` |
