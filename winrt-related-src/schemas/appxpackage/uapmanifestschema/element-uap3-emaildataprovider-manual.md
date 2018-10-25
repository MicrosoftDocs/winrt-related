---
Description: Declares an app extensibility point of type windows.emailDataProvider.
Search.Product: eADQiWindows 10XVcnh
title: uap3:EmailDataProvider (Windows 10)
ms.assetid: 113e2e55-a05b-4bb7-9091-5d8f92272103
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# uap3:EmailDataProvider (Windows 10)


Declares an app extensibility point of type **windows.emailDataProvider**.

This element enables apps to become data providers for email. A data provider is an application that can fully replace the built-in synchronization engine for email as the synchronization engine for an account. A data provider can not only synchronize the data associated with the account, but can also provide implementations for secondary APIs, such as those required to compose Secure/Multipurpose Internet Mail Extensions (S/MIME) messages or perform server searches on behalf of another application.

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
<dd><b>&lt;uap3:EmailDataProvider&gt;</b></dd>
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
<uap3:EmailDataProvider ServerName? = A string between 1 and 32767 characters in length 
                                      with a non-whitespace character at its beginning 
                                      and end. >
</uap3:EmailDataProvider>
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
                <uap3:Extension Category="windows.emailDataProvider" 
                                EntryPoint="UserDataProvider.EmailDataProviderTask">  
                    <uap3:EmailDataProvider ServerName="MyDataProvider.PPLE" />  
                </uap3:Extension> 
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                            |
|---------------|------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/uap/windows10/3 |

 

 

 



