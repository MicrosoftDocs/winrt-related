---

title: UAP10:MediaContentDecryptionModule
description: Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files.

ms.date: 03/14/2022
ms.topic: reference

keywords: windows 10, uwp, schema, manifest, extension 
---

# UAP10:MediaContentDecryptionModule

Defines an extension for a desktop app in an MSIX package that defines decryption information to be used to access media files.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap10-extension">&lt;UAP10:Extension&gt;</a></dt>
<dd><b>&lt;UAP10:MediaContentDecryptionModule&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```
<uap10:MedicaContentDecryptionModule DisplayName = A string with a value between 1 and 256 characters in length.
                                     Description = A string with a value between 1 and 2048 characters in length.
                                     SupportedKeySystems = A string with a value between 1 and 255 characters in length.
                                     ActivatableClassId = A string with a value between 1 and 255 characters in length.
                                     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, ", &, |, ?, or *.
                                     ProcessorArchitecture = A string value that can be one of the following: "x86", "x64", "arm", "arm64", "neutral"
                                     >

</uap10:MedicaContentDecryptionModule>
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | A user-friendly display name for the media content. | A string with a value between 1 and 256 characters in length. | Yes |
| Description | A user-friendly description for the media content. | A string with a value between 1 and 2048 characters in length. | Yes |
| Supported Key Systems | Defines the key systems used to encrypt/descrypt media content. | A string with a value between 1 and 255 characters in length. | Yes |
| rescap3:ActivatableClassId | The class ID associated with this media content. | A string with a value between 1 and 255 characters in length. | No |
| rescap3:Path | The path to the media content. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, ", &#124;, ?, or *. | No |
| rescap3:ProcessorArchitecture | The processor architecture used for the media content. | A string value that can be one of the following: "x86", "x64", "arm", "arm64", "neutral" | No

## Requirements
|   | Value |
|--|--|
| **uap10** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
| **rescap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/windowscapabilities/3` |