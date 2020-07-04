<div class="h2"><?php gettext('Łączymy sektor publiczny 
z najlepszymi pomysłami przedsiębiorców')?></div>


<div class="row">
  <div class="col-md-8 offset-md-2  text-left ">
<ul class="nav nav-tabs nav-tabs-start">
<li class="nav-item nav-item-start">
<a class="nav-link nav-link-start active" href="<?php echo base_url();?>"><?php gettext('DLA OSÓB I FIRM')?></a>
</li>
<li class="nav-item">
<a class="nav-link nav-link-start" href="<?php echo base_url('start/sektor_publiczny');?>"><?php gettext('DLA SEKTORA PUBLICZNEGO')?></a>
</li>
</ul>
  </div>
</div>


<div class="row header-logo">
  <div class="col-md-8 offset-md-2 my-5 text-left">
    <div class="logo1"></div>
    <div class="h2"><?php gettext('Łączymy sektor publiczny 
z najlepszymi pomysłami przedsiębiorców')?></div>
    <a class="btn  btn-outline-primary mt-5" href="#konkursy"><?php gettext('PODEJMIJ WYZWANIE TECHNOLOGICZNE')?></a>
  </div>
</div>

<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
  <h1 class="h2"><?php gettext('Usuwanie postępowania z obserwowanych ')?></h1>
</div>


<?php

$attributes = array('class'=>'form' );
?>

<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
  <h1 class="h2"><?php gettext('Ustaw płatne wsparcie Operatora')?></h1>
</div>

<?php
  echo form_open(current_url(),$attributes);
?>


            <hr class="mb-4">
      <div class="row justify-content ">
        <div class="col-md-2 ">
            <a href="<?php echo base_url('postepowania')?>" class="btn btn-outline-secondary btn-block" ><?php gettext('Wróć')?></a>
        </div>
        <div class="col-md-5 ">
            <input class="btn btn-primary btn-block" type="submit" name="cancel" value="Anuluj płatne wsparcie">
        </div>
        <div class="col-md-5 ">
            <input class="btn btn-primary btn-block" type="submit" name="proceed" value="Ustaw płatne wsparcie">
        </div>
      </div>
          </form>

          <!doctype html>
<html lang="pl">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Platforma Konkursowa GovTech">
    <meta name="author" content="hostlab.pl">
    <link rel="icon" type="image/ico" sizes="16x16" href="<?php echo base_url('assets/images/favicon.ico')?>">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i&amp;subset=latin-ext" rel="stylesheet">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="theme-color" content="#ffffff">

    <title><?php gettext('GovTech - Zaloguj się')?></title>

    <link href="<?php echo site_url('assets/css/bootstrap.min.css')?>" rel="stylesheet">
    <link href="<?php echo site_url('assets/css/signin.css')?>" rel="stylesheet">

    
    
    
    
    
    
<!-- Google Tag Manager -->

<!-- End Google Tag Manager -->
<!-- Hotjar Tracking Code for https://konkursy.govtech.gov.pl -->

  </head>

  <body class="text-center">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KSQK3DB"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
  <div class="container-fluid">
      <?php /* ?>
      <div class="row justify-content-right">
        <div class="col-md-12 text-center">
<a href="#" class="changeThemeColour changeLink"><span data-feather="eye"></span><?php gettext(' Wersja dla słabo widzących')?></a>
 &nbsp; <a href="#" class="changeFontSize changeLink"><span data-feather="zoom-in"></span><?php gettext(' Powiększ tekst')?></a>
        </div>
      </div>
      <?php */ ?>
    <div class="row header-logo">
      <div class="col-md-8 offset-md-2 my-5 text-left">
        <div class="h2"><strong><?php gettext('Platforma GovTech')?></strong></div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-8 offset-md-2 mt-2 text-left">

      <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item" style="margin-top: -2px;"><a href="https://govtech.gov.pl"><span data-feather="home"></span></a></li>
          <li class="breadcrumb-item"><a href="<?php echo base_url()?>"><?php gettext('Platforma GovTech')?></a></li>
          <li class="breadcrumb-item active" aria-current="page"><?php gettext('Logowanie')?></li>
        </ol>
      </nav>

      </div>
    </div>
    <div class="row">
      <div class="col-md-8 offset-md-2 my-2 text-left">
        <div class="h3 mb-4"><strong><?php gettext('Zaloguj się na Plaformę GovTech')?></strong></div>
<?php if($_counter>7 || $_login_failure_count>7){ ?>

<?php } ?>
<?php
$attributes = array('class'=>'form-signin');
echo form_open(site_url('login'),$attributes);

//<img class="mb-4 pb-5" src="< ?php echo site_url('assets/images/logo_govtech_pl.png')? >" alt="GovTech" style="max-width:275px;">

?>

<?php
echo $info_msg;
?>


      <?php echo form_error('user_email'); ?>
      <label for="inputEmail" ><?php gettext('Adres email')?></label>
      <input type="email" id="inputEmail" class="form-control" placeholder="Adres email" name="user_email" required autofocus>
      <?php echo form_error('user_password'); ?>
      <label for="inputPassword" class="mt-2"><?php gettext('Hasło')?></label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Hasło" name="user_password" required>
<?php if($_counter>7 || $_login_failure_count>7){ ?>
      <div class="mb-3">
        <label for="recaptcha-field" class="mt-2"><?php gettext('Kod zabezpieczający')?></label>
        <?php echo form_error('g-recaptcha-response'); ?>


<div id="recaptcha-field" class="g-recaptcha"></div>

      </div>
<?php } ?>
      <div class="links text-left mb-5">
      <a href="<?php echo site_url('haslo')?>" ><?php gettext('Odzyskaj hasło')?></a>
      </div>
      <div class="row">
        <div class="col-md-6 align-middle">
        <a class="btn-link btn-block mt-1" href="<?php echo site_url('rejestracja')?>" ><?php gettext('Zarejestruj się')?></a>
        </div>
        <div class="col-md-6">
        <button class="btn btn-primary btn-block" type="submit"><?php gettext('Zaloguj się')?></button>
        </div>
      </div>
    </form>
<?php if($_counter>7 || $_login_failure_count>7){ ?>

<?php } ?>
      </div>
    </div>


<?php echo $this->load->view('stopka_niezalogowany_view', array(), true);	  ?>

  </div>
    <!-- Icons -->
    
    

<!-- Ybug code -->

<!-- Ybug code end -->
  </body>
</html>
