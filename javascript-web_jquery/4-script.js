#!/usr/bin/node
/* global $ */

$(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
