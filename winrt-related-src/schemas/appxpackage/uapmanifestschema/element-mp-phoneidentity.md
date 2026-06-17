---
title: mp:PhoneIdentity
description: Provides information about an app previously made available on Windows Phone.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, mp:Package, mp:PhoneIdentity]
---

# mp:PhoneIdentity

If your app is an update to an app previously made available on Windows Phone, ensure that this element matches what is in the app manifest of your previous app. Use the same GUIDs that were assigned to the app by the Store. This ensures that users of your app who are upgrading to Windows 10 will receive your new app as an update, and not as a duplicate.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ **`<PhoneIdentity>`**  

## Syntax

```xml
<mp:PhoneIdentity
  PhoneProductId = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  PhonePublisherId = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **PhoneProductId** | A unique identifier for a mobile product. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **PhonePublisherId** | <!-- TODO: Add description --> | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Package](element-f-package.md) | Defines the root element of an app package manifest. The manifest describes the structure and capabilities of the software to the system. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/2014/phone/manifest` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

For apps that are not migrating from a mobile version, the **PhoneProductId** and **PhonePublisherId** are required for Store submission but are not validated. For project types that require the **PhoneIdentity** element, the Visual Studio project templates should include placeholder values. If you created a project from a template that does not include these values, you can specify any GUID for **PhoneProductId** and the value "00000000-0000-0000-0000-000000000000" for  **PhonePublisherID**.

## Examples

<!-- Author content goes here -->
