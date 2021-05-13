---

title: uap5:Host
description: Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:Host
Represents a valid HTTP or HTTPS host name with a wildcard that the app wants to register as able to handle.

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
<dd>
<dl>
<dt><a href="element-uap3-appurihandler-manual.md">&lt;uap3:AppUriHandler&gt;</a></dt>
<dd><b>&lt;uap5:Host&gt;</b></dd>
</dl>
</dd>
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
<uap5:Host Name = A wildcard with a domain name of the web site associated with the app. />
```

## Attributes and Elements


**Attributes**

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| **Name**  | A wildcard with a domain name of the web site associated with the app. | A wildcard and a period (*.) followed an alphanumeric domain name string. | Yes  |    

 

**Child Elements**

None.

**Parent Elements**

| Parent Element | Description |
|----------------|-------------|
| [**uap3:AppUriHandler**](element-uap3-appurihandler-manual.md) | Declares an app extensibility point of type **windows.appUriHandler**. |

 

## Examples
In this example, *.microsoft.com can handled as: docs.microsoft.com, developer.microsoft.com, foo.microsoft.com, etc.

```XML
<Package ...
         xmlns:uap3="http://schemas.microsoft.com/appx/manifest/uap/windows10/3"  
         xmlns:uap5="http://schemas.microsoft.com/appx/manifest/uap/windows10/5"  
         IgnorableNamespaces="... uap3">
    <Applications>
        <Application>
            <Extensions>
                <uap3:Extension Category="windows.appUriHandler">  
                    <uap3:AppUriHandler>  
                        <uap5:Host Name="*.microsoft.com" />  
                    </uap3:AppUriHandler>  
                </uap3:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements

|               | Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
