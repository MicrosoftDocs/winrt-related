---
description: Declares an app extensibility point of type windows.contactDataProvider.
Search.Product: eADQiWindows 10XVcnh
title: uap3:ContactDataProvider
ms.assetid: 8ae46d6c-d198-4472-9533-e99999cfe5ca


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:ContactDataProvider


Declares an app extensibility point of type **windows.contactDataProvider**.

This element enables apps to become data providers for contacts. A data provider is an application that can fully replace the built-in synchronization engine for the contacts as the synchronization engine for an account. A data provider can not only synchronize the data associated with the account, but can also provide implementations for secondary APIs, such as those required to compose Secure/Multipurpose Internet Mail Extensions (S/MIME) messages or perform server searches on behalf of another application.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap3-extension-manual.md">&lt;uap3:Extension&gt;</a></dt>
<dd><b>&lt;uap3:ContactDataProvider&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<uap3:ContactDataProvider ServerName? = A string between 1 and 32767 characters in length 
                                        with a non-whitespace character at its beginning 
                                        and end. >
</uap3:ContactDataProvider>
```

**Key**

          ? optional (zero or one)

## Attributes and Elements


**Attributes**

| Attribute      | Description                                                                                                                                                                                                     | Data type                                                                                                   | Required | Default value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------|---------------|
| **ServerName** | The COM server to be instantiated to satisfy the contract activation (ensures that only one instance of the server exists at runtime). This is an optional attribute that is only used for PPLE host processes. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No       |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                 | Description                                  |
|------------------------------------------------|----------------------------------------------|
| [**uap3:Extension**](element-1-extensions.md) | Declares an extensibility point for the app. |

 

## Examples


```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.contactDataProvider" 
                                EntryPoint="UserDataProvider.ContactDataProviderTask" />  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/3` |

 

 

 



