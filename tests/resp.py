"""Mock response elements."""

# Standard library imports
from dataclasses import dataclass


# This is a sample response body returned from MED.
resp_text = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

    <!-- Mobile viewport optimization h5bp.com/ad -->
    <meta name="HandheldFriendly" content="True">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">

    <!-- Internet Explorer use the highest version available -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <!-- Mobile IE allows us to activate ClearType technology for smoothing fonts for easy reading -->
    <!--[if IEMobile]>
      <meta http-equiv="cleartype" content="on">
    <![endif]-->
    <!-- <title>MiddleEnglishDictionary</title> -->
    <title>a - Middle English Compendium</title>
    <link rel="shortcut icon" type="image/x-icon" href="/m/middle-english-dictionary/assets/favicon-b98d73b9b7fbd65536579286c407fe5c077705485cc1a060a6dfafbca133b2f3.ico" />

    <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="o6t/57mZgCfhH17t47lH6Ifh/aLSmjGLACJe35JDIjx/mZIkv5dXla37aYRnYyVozzaeOgFqhdflnYeb5VbbNw==" />

    <link rel="stylesheet" media="all" href="/m/middle-english-dictionary/assets/application-a4cf7edcf39f1a508d055a350c96390eecf7bf7bc7b9ca48576e2dcb63115121.css" />
    <script src="/m/middle-english-dictionary/assets/application-5e003b6459e1c7e4c059a65a027753090b8919d185ea3fec6de086cd7f7c75d6.js"></script>
    

    <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-43730774-3"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-43730774-3');
</script>


  </head>
    
  <body class="blacklight-catalog blacklight-catalog-show" >

    
        <header class="site-header">
  <div id="header-navbar" class="navbar navbar-inverse navbar-static-top" role="navigation">

    <div class="container container--full site-header-container">
      <div class="site-title-container">
        <a href="/m/middle-english-dictionary" class="site-link site-title-flex"><img class="site-logo" src="https://apps.lib.umich.edu/falafel/v0/graphics/mlib_square__transparent.svg" alt="University of Michigan"><span class="site-title">Middle English Compendium</span></a>
      </div>
       <button type="button" class="navbar-toggle btn collapsed" data-toggle="collapse" data-target="#user-util-collapse">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      </button>

      

      <div class="collapse navbar-collapse" id="user-util-collapse">
        <div class="navbar-right">
  <ul class="nav navbar-nav">
    


  </ul>
</div>

      </div>
    </div>

    <div id="header-navbar-secondary" role="navigation">
      <div class="container container--full site-header-container">
            


<ul class="header-nav-secondary">
   <li class="active" aria-current="page"><a href="/m/middle-english-dictionary/dictionary">Dictionary</a>
</li>
   <li ><a href="/m/middle-english-dictionary/bibliography">Bibliography</a>
</li>
   <li ><a href="/m/middle-english-dictionary/quotations">Quotations</a>
</li>

</ul>

      </div>
    </div>

  </div>
</header>



  <div class="search-bar--header">
      <div id="search-bar" class="container">
          <form class="search-query-form clearfix navbar-form" role="search" action="/m/middle-english-dictionary/dictionary" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
  
  <div class="input-group">
      <span class="input-group-addon for-search-field">
        <label for="search_field" class="sr-only">Search in</label>
        <select name="search_field" id="search_field" title="Targeted search options" class="search_field"><option value="anywhere">Entire entry</option>
<option selected="selected" value="hnf">Headword (with alternate spellings)</option>
<option value="h">Headword (preferred spelling only)</option>
<option value="notes_and_def">Definition and notes</option>
<option value="etyma">Etymology</option>
<option value="citation">Associated quotes and manuscripts</option>
<option value="oed">Modern English word equivalent</option></select>
      </span>

    <div class="search-input-group">
      <label for="q" class="sr-only">search for</label>
      <input type="text" name="q" id="q" placeholder="Search..." class="search_q q form-control" data-autocomplete-controller="search_field" data-autocomplete-config="hithere" data-autocomplete-enabled="false" data-autocomplete-path="/m/middle-english-dictionary/m/middle-english-dictionary/suggest" />

      <!--Keyboard drop down for special characters-->
      <span class="dropdown keyboard">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <img alt="Drop down menu for special character selection" src="/m/middle-english-dictionary/assets/keyboard-grey-1a43c1453cdd01cf8e681254c0cdf2a8771520ff7b96eefa52b6d0c3fea28ccf.svg" />
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          <ul class="keyboard-list">
            <li><a href="#" id="thorn" class="dropdown-item" role="button" >Þ þ (thorn)</a></li>
            <li><a href="#" id="eth" class="dropdown-item" role="button" >Ð ð (eth)</a></li>
            <li><a href="#" id="yogh" class="dropdown-item" role="button" >Ʒ ʒ (yogh)</a></li>
            <li><a href="#" id="ash" class="dropdown-item" role="button" >Æ æ (ash)</a></li>
          </ul>
        </div>
      </span>

      <span class="input-group-btn">
        <button type="submit" class="btn btn-primary search-btn" id="search">
          <span class="submit-search-text">Search</span>
          <span class="glyphicon glyphicon-search"></span>
        </button>
      </span>
    </div>
  </div>
</form>
      </div>
  </div>


    

    <div class="container">

      
        <div class="row">
          <div class="col-md-9 col-md-offset-3 col-sm-8 col-sm-offset-4 col-xs-12">
            <h1></h1>
          </div>
        </div>

      <div class="row">
        <div id="sidebar" class="col-md-3 col-sm-4 col-xs-12">
   
  <div class="panel panel-default">
    <h3 class="panel-heading">Related Dictionary Entries</h3>
    <div class="panel-body">

        <div class="related-link-subhead">Oxford English Dictionary</div>
        <p class="oed-subscription-warning">(Please note that the OED is a
          subscription resource)</p>
        <ul>
            <li>
              <a class="external-link" href=http://www.oed.com/view/Entry/1>a
                <img alt="Opens in a new window" src="/m/middle-english-dictionary/assets/external-link-blue-622a2080eed310c988c4462b76250bc28f3056e81fbd9b461b73ca2a1d9c6b99.svg"></a>
            </li>
        </ul>

        <div class="related-link-subhead">Dictionary of Old English</div>
        <ul>
            <li>
              <a class="external-link" href=http://tapor.library.utoronto.ca/doe/?E00036>a noun
                <img alt="Opens in a new window" src="/m/middle-english-dictionary/assets/external-link-blue-622a2080eed310c988c4462b76250bc28f3056e81fbd9b461b73ca2a1d9c6b99.svg"></a>
            </li>
        </ul>

    </div>
  </div>



</div>

<div id="content" class="col-md-9 col-sm-8 col-xs-12 show-document">
  <div id='previousNextDocument' class='pagination-search-widgets'>
    <!-- <div class="page_links"> -->
       <!-- | -->

       <!-- | -->

    <!-- </div> -->
    <div class="pull-left search-widgets">

      <a id="startOverLink" class="btn" href="/m/middle-english-dictionary/dictionary">Start Over</a>

    </div>

</div>



<div id="document" class="document blacklight-entry" itemscope  itemtype="http://schema.org/Thing">
  <div id="doc_med1">
    

<div class="entry-panel">

  <h2 class="entry-main-title">Middle English Dictionary Entry</h2>

  <div class="entry-heading">
    <div class="entry-container">
      <div class="entry-headword">
        ā&nbsp;<span class="entry-pos">n.(1)</span>
      </div>

        <div class="quotations-header-options">
          <span class="quotations-header-options-text">Quotations:</span>
          <a class="show-all-button" href="#" onClick="$('.egs').show(); $('.quote-toggle.open').hide(); $('.quote-toggle.closer').show();return false;">Show
            all</a>
          <a class="hide-all-button" href="#" onClick="$('.egs').hide(); $('.quote-toggle.open').show(); $('.quote-toggle.closer').hide(); return false">Hide
            all</a>
        </div>
    </div>
  </div>

  <div>
    <h3 class="entry-intro-title">Entry Info</h3>
  </div>

  <div class="entry-info">
    <table class="table table-striped">
      <tr>
        <td class="forms-title">Forms</td>
        <td>
          <span class="FORM"><span class="HDORTH">ā</span> <span class="POS"> n.(1) </span></span>

        </td>
      </tr>
      <tr>
        <td class="etymology-title">Etymology</td>
        <td class="etymology-list">
          
        </td>
      </tr>
    </table>
  </div>



  <div class="senses">
    <h3 class="entry-senses-title">Definitions (Senses and Subsenses)</h3>

    
<div class="sense">
      


<div class="sense">
  <div class="entry-senses">
    <div class="sense-number">1.</div>
      <div class="definition">(a) The letter A of the alphabet; cp. <span class="HI_B">a-per-se</span>; (b) the letter A used in enumeration, in labeling a diagram or a square on the chess board, the recto of a folio, a star, etc.; (c) the dominical letter A.


      <div class="quote-toggles">
        <a class="quote-toggle 1-0-toggle open" href="#" onClick="$('.1-0-toggle').toggle(); return false">Show&nbsp;13&nbsp;Quotations</a>
        <a class="quote-toggle  1-0-toggle closer collapsed" href="#" onClick="$('.1-0-toggle').toggle(); return false">Hide&nbsp;13&nbsp;Quotations</a>
      </div>
    </div>
  </div>

  <div class="egs collapsed 1-0-toggle">
    <h4>Associated quotations</h4>
      <div class="eg">
          <div class="subdef-entry-number">a</div>
        <div class="citations">
          <ul>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB2677?rid=HYP.733.19981211T105002"><span class="DATE">c1175</span> <span class="TITLE">Orm.</span><span clas="MS">(Jun 1)</span></a></span><span class="SCOPE">16434</span></span>
: <span class="Q">Þe firrste staff iss nemmnedd A Onn ure Latin spæche. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB3469?rid=HYP.1614.19981211T105002"><span class="DATE">(a1398)</span> *<span class="AUTHOR">Trev.</span><span class="TITLE">Barth.</span><span clas="MS">(Add 27944)</span></a></span><span class="SCOPE">8a/a</span></span>
: <span class="Q">I lerned a and Be And oþir lettres by here names. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB3432?rid=HYP.1574.19981211T105002"><span class="DATE">(1402)</span> <span class="TITLE">Topias</span> <span clas="MS">(Dgb 41)</span></a></span><span class="SCOPE">p.57</span></span>
: <span class="Q">I know not an a from the wynd-mylne, ne a b from a bole foot. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB625?rid=HYP.1500.19990513T124835"><span class="DATE">a1425(c1385)</span> <span class="AUTHOR">Chaucer</span> <span class="TITLE">TC</span> <span clas="MS">(Benson-Robinson)</span></a></span><span class="SCOPE">1.171</span></span>
: <span class="Q">Right as oure firste lettre is now an A. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB629?rid=HYP.227.19991101T123123"><span class="DATE">?a1425</span> *<span class="TITLE">Chauliac(1)</span> <span clas="MS">(NY 12)</span></a></span><span class="SCOPE">176b/b</span></span>
: <span class="Q">Medicynes bigynnyng by A A A. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB1636?rid=HYP.207.20011127T144602"><span class="DATE">a1475</span> <span class="TITLE">Inf.Chr.</span><span clas="MS">(Hrl 3954)</span></a></span><span class="SCOPE">197</span></span>
: <span class="Q">Now qwy is a beforn þe b? </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB108?rid=HYP.113.19990513T124835"><span class="DATE">(1448)</span> <span class="TITLE">Acc.St.Mary Thame</span> in <span class="TITLE">BBOAJ 13</span></a></span><span class="SCOPE">49</span></span>
: <span class="Q">The orfray contenyng A and M crownyt. </span></span>
</li>
          </ul>
        </div>

      </div>
      <div class="eg">
          <div class="subdef-entry-number">b</div>
        <div class="citations">
          <ul>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB263?rid=HYP.360.19990513T124835"><span class="DATE">(1340)</span> <span class="TITLE">Ayenb.</span><span clas="MS">(Arun 57)</span></a></span><span class="SCOPE">1</span></span>
: <span class="Q">A betocneþ þe uerste half of þe leave, b þe oþerhalf. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB3447?rid=HYP.1588.19981211T105002"><span class="DATE">?c1400</span> <span class="TITLE">Treat.Geom.</span><span clas="MS">(Sln 213)</span></a></span><span class="SCOPE">65</span></span>
: <span class="Q">Make a quadrat..in þe manner of ABCD..and wite you that A es þe right cornel vpward. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB570?rid=HYP.612.19990513T124835"><span class="DATE">c1400</span> *<span class="AUTHOR">Chaucer</span> <span class="TITLE">Astr.</span><span clas="MS">(Brussels 4869)</span></a></span><span class="SCOPE">2.23.90a</span></span>
: <span class="Q">Clepe that sterre A. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB1830?rid=HYP.427.20011127T144602"><span class="DATE">(a1425)</span> in Strutt <span class="TITLE">Dress</span></a></span><span class="SCOPE">2.97</span></span>
: <span class="Q">[In the manner of laces making..the first finger next the thumb shall be called] A [the second finger] B. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB635?rid=HYP.244.19991101T123123"><span class="DATE">a1475</span> <span class="TITLE">Chess(1)</span> <span clas="MS">(Porter)</span></a></span><span class="SCOPE">602</span></span>
: <span class="Q">Sey chec; þen he goys in to A. </span></span>
</li>
          </ul>
        </div>

      </div>
      <div class="eg">
          <div class="subdef-entry-number">c</div>
        <div class="citations">
          <ul>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB388?rid=HYP.547.19990513T124835"><span class="DATE">c1450(c1430)</span> <span class="TITLE">Brut-1430</span> <span clas="MS">(Glb E.8)</span></a></span><span class="SCOPE">436/34</span></span>
: <span class="Q">On Seint Lethenardis day..on the Sonday (and Sonday went by lettur A that yere), the Kynge was crownyd. </span></span>
</li>
          </ul>
        </div>

      </div>
  </div>

</div>

      


<div class="sense">
  <div class="entry-senses">
    <div class="sense-number">2.</div>
      <div class="definition">A sound represented by the letter A.


      <div class="quote-toggles">
        <a class="quote-toggle 2-1-toggle open" href="#" onClick="$('.2-1-toggle').toggle(); return false">Show&nbsp;6&nbsp;Quotations</a>
        <a class="quote-toggle  2-1-toggle closer collapsed" href="#" onClick="$('.2-1-toggle').toggle(); return false">Hide&nbsp;6&nbsp;Quotations</a>
      </div>
    </div>
  </div>

  <div class="egs collapsed 2-1-toggle">
    <h4>Associated quotations</h4>
      <div class="eg">
        <div class="citations">
          <ul>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB2718?rid=HYP.788.19981211T105002"><span class="DATE">a1425(a1400)</span> <span class="TITLE">PConsc.</span><span clas="MS">(Glb E.9 &amp; Hrl 4196)</span></a></span><span class="SCOPE">481</span></span>
: <span class="Q">When it es born it cryes swa: If it be man it says 'a, a', Þat þe first letter es of þe nam Of our formefader Adam. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB2718?rid=HYP.788.19981211T105002"><span class="DATE">a1425(a1400)</span> <span class="TITLE">PConsc.</span><span clas="MS">(Glb E.9 &amp; Hrl 4196)</span></a></span><span class="SCOPE">494</span></span>
: <span class="Q">Alle þas..þat comes of Eve..When þai er born, what-swa þai be, Þai say outher a, a or e, e. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB181?rid=HYP.199.19990513T124835"><span class="DATE">c1450</span> <span class="TITLE">Alph.Tales</span> <span clas="MS">(Add 25719)</span></a></span><span class="SCOPE">275/16</span></span>
: <span class="Q">He cuthe not als mekull as say A, þat is þe furst vowell. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB279?rid=HYP.379.19990513T124835"><span class="DATE">c1450</span> <span class="TITLE">Battlefield Gram.</span><span clas="MS">(Trin-C O.5.4)</span></a></span><span class="SCOPE">111</span></span>
: <span class="Q">How many coniugacions hastowe? Foure. The ffyrste ys that hath an a longe by fore the re or the ri in the jnfinityf mode. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB2418?rid=HYP.424.19981211T105002"><span class="DATE">a1500(?a1390)</span> <span class="AUTHOR">Mirk</span> <span class="TITLE">Fest.</span><span clas="MS">(GoughETop 4)</span></a></span><span class="SCOPE">157/2</span></span>
: <span class="Q">Wythout on of þos v lettyrs þer may no man know what anoþyr spekeþe; and þes ben þe lettres: A, E, I, O, V. </span></span>
</li>
              <li class="citation-list-item"><span class="CIT"><span class="BIBL"><span class="STNCL"><a href="/m/middle-english-dictionary/bibliography/BIB3300?rid=HYP.651.19990304T151115"><span class="DATE">a1500</span> <span class="TITLE">Donatus (1)</span> <span clas="MS">(StJ-C F.26)</span></a></span><span class="SCOPE">1024</span></span>
: <span class="Q">Þe furst coniugacyon..hath a long be-forn þe -re in þe infenityf. </span></span>
</li>
          </ul>
        </div>

      </div>
  </div>

</div>

      
<h3 class="entry-supplemental-title">Supplemental Materials (draft)</h3>
<div class="supplements-all">
    <div class="entry-supplement">
      <div class="SUPPLEMENT"><ul>
<li><span class="CIT"><span class="BIBL"><span class="STNCL"><span class="DATE">a1425</span> *<span class="TITLE">Tit.Alphabet</span> <span clas="MS">(Tit D.17)</span></span><span class="SCOPE">9a</span></span>
: <span class="Q">Alphabetum Anglicum: A, a; b, be. </span></span></li>
<div class="NOTE"> <span class="note-title">Note: </span>1st occurrence sense <span class="HI_B">1.</span>(a) - date covered; 2nd occ. <span class="HI_B">1.</span>(b). Date covered in both senses</div>
</ul></div>

    </div>
</div>


</div>



  </div>


</div>

  </div>
</div>


</div>
      </div>

    </div>


    <footer class="footer footer--dark ">
  <div class="footer-container footer-text--light">
    <section>
      <ul>
        <li class="heading-medium">Middle English Compendium</li>
        <li><a href="/m/middle-english-dictionary/dictionary">Middle English Dictionary</a></li>
        <li><a href="/m/middle-english-dictionary/bibliography">Bibliography</a></li>
        <li><a href="https://quod.lib.umich.edu/c/cme/" target="_blank">Corpus <img alt="Opens in a new window" src="/m/middle-english-dictionary/assets/external-link-white-7985672493f04071f2276be1763f854890cd979f17f5857d7b8634db19f28f5d.svg" /></a></li>
      </ul>
     </section>
    <section>
     
      <ul>
        <li class="heading-medium">Help and information</li>
        <li><a href="/m/middle-english-dictionary/help">Search Help</a></li>
        <li><a href="/m/middle-english-dictionary/about">About the MEC</a></li>
      </ul>
     </section>
     <section>
      <ul>
        <li class="heading-medium">Contact Us</li>
        <li><a href="https://umich.qualtrics.com/jfe/form/SV_43fHANnBfEOjO4J">Contact Us</a></li>
        <li><a href="mailto:mec-info@umich.edu">mec-info@umich.edu</a></li>
      </ul>

     </section>
  </div>
</footer>
<div class="footer-subfooter footer--light">
   <div class="footer-container">
      <p class="font-xsmall">©2022  Regents of the University of Michigan.
        For details about this collection's copyright
        see the <a href="/m/middle-english-dictionary/about#copyright">MEC copyright statement</a>
        and the
        <a href="https://www.lib.umich.edu/library-administration/library-copyright-statement">U-M Library Copyright Policy</a>.
    Data last refreshed November 2019.
     </p>
    </div>
</div>




  </body>
</html>
"""


@dataclass
class MockResp:
    text: str = resp_text

    def raise_for_status(self) -> None:
        return None

    @property
    def status_code(self) -> int:
        return 200
