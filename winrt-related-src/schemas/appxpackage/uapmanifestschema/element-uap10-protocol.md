---

title: UAP10:Protocol
description: Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

ms.date: 03/14/2022
ms.topic: reference

keywords: windows 10, uwp, schema, manifest, extension 
---

# UAP10:Protocol

Declares an app extensibility point of type windows.protocol. A URI association indicates that the app is registered to handle URIs with the specified scheme.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-extension">&lt;UAP10:Extension&gt;</a></dt>
<dd><b>&lt;UAP10:Protocol&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```
<uap10:Protocol       name = A string between 2 and 2048 characters in length.
                      desiredView? = A string value that can be one of the following: "default", "useLess", "useHalf", "useMore", "useMinimum"
                      returnResults? = A string value that can be one of the following: "none", "always", "optional"
                      parameters? = A string value or set of string values between % characters.
                      >

  <!-- Child elements -->
  ( uap10:Logo )
  ( uap10:DisplayName )
  ( rescap3:MigrationProgIds )
  ( previewappcompat:ProgId )

</uap10:Protocol>
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | A user-friendly display name for the media content. | A string between 2 and 2048 characters in length. | Yes |
| Desired View | A user-friendly description for the media content. | A string value that can be one of the following: "default", "useLess", "useHalf", "useMore", "useMinimum". | No |
| Return Results | Defines the key systems used to encrypt/descrypt media content. | A string value that can be one of the following: "none", "always", "optional". | No |
| Parameters | The class ID associated with this media content. | A string value or set of string values between % characters. | No |

## Child Elements
| Child Element | Description |
|---------------|-------------|
| [Logo](element-uap10-logo.md) | The logo used for application icons during packaging. |
| [DisplayName](element-uap10-displayname.md) | The display name used for the application. |
| [rescap3:MigrationProgIds](element-rescap3-migrationprogids.md) | The program IDs used for migrations for the application.
| [previewAppCompat:ProgId](element-previewappcompat-progid.md) | The program ID used for application compatibility previews for the application.

## Requirements
|   | Value |
|--|--|
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **rescap4** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities/4` |
| **previewappcompat** | `http://schemas.microsoft.com/appx/manifest/preview/windows10/msixappcompatsupport/3` |