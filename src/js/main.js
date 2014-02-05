var BaseView = Backbone.View.extend({

  el:'#reg',
  render: function(){
    this.$el.html('<h1>BB.Is.Working!</h1>');
  }
});

var v = new BaseView();

v.render();