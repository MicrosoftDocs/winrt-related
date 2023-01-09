---
description: Provides information about an app previously made available on Windows Phone.
Search.Product: eADQiWindows 10XVcnh
title: mp:PhoneIdentity (Windows 10)
ms.assetid: 817d5865-3838-4554-b751-2af09d84c8ad
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# mp:PhoneIdentity (Windows 10)

If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;**\<mp:PhoneIdentity\>**

## Syntax

```xml
<PhoneIdentity
  PhoneProductId = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  PhonePublisherId = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **PhoneProductId** | A unique identifier for a mobile product. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **PhonePublisherId** | Describes the publisher information for a mobile product. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Package](element-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Remarks

For apps that are not migrating from a mobile version, the **PhoneProductId** and **PhonePublisherId** are required for Store submission but are not validated. For project types that require the **PhoneIdentity** element, the Visual Studio project templates should include placeholder values. If you created a project from a template that does not include these values, you can specify any GUID for **PhoneProductId** and the value "00000000-0000-0000-0000-000000000000" for  **PhonePublisherID**.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/2014/phone/manifest` |
