---
title: uap3:FileTypeAssociations
description: Defines the types of files used within the application.
ms.date: 03/14/2022

ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap3:FileTypeAssociations

Defines the types of files used within the application.

[ <  Package  > ](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Applications > ](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < Application > ](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ < UAP3:Extension > ](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**< UAP3:FileTypeAssociations >**

## Syntax
```syntax
<uap3:FileTypeAssociations Parameters? = A string value between 1 and 32767 characters.
                   Multi-Select Model? = A string value that can be any one of the following: "Player", "Document", or "Single".>

</uap3:FileTypeAssociations>
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Parameters | Specifies parameters to define the types of files used in the application. | A string value between 1 and 32767 characters. | No |
| Multi-Select Model | Specifies the model used to define the types of files used in the application. | A string value that can be any one of the following: "Player", "Document", or "Single". | No |

## Child Elements

None.

## Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [uap3:Extension](element-uap3-extension-manual.md) | Sets parameters to define the protocol of the extensions. |

## Requirements
|   | Value |
|--|--|
| **uap3** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |