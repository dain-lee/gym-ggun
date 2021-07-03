!(function ($) {
    'use strict';

    var CalendarApp = function () {
        this.$body = $('body');
        (this.$calendar = $('#calendar')),
            (this.$event = '#calendar-events div.calendar-events'),
            (this.$categoryForm = $('#add-new-event form')),
            (this.$extEvents = $('#calendar-events')),
            (this.$modal = $('#my-event')),
            (this.$saveCategoryBtn = $('.save-category')),
            (this.$calendarObj = null);
    };

    /* on drop */
    (CalendarApp.prototype.onDrop = function (eventObj, date) {
        var $this = this;
        // retrieve the dropped element's stored Event Object
        var originalEventObject = eventObj.data('eventObject');
        var $categoryClass = eventObj.attr('data-class');
        // we need to copy it, so that multiple events don't have a reference to the same object
        var copiedEventObject = $.extend({}, originalEventObject);
        // assign it the date that was reported
        copiedEventObject.start = date;
        if ($categoryClass) copiedEventObject['className'] = [$categoryClass];
        // render the event on the calendar
        $this.$calendar.fullCalendar('renderEvent', copiedEventObject, true);
        // is the "remove after drop" checkbox checked?
        if ($('#drop-remove').is(':checked')) {
            // if so, remove the element from the "Draggable Events" list
            eventObj.remove();
        }
    }),
        (CalendarApp.prototype.enableDrag = function () {
            //init events
            $(this.$event).each(function () {
                // create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
                // it doesn't need to have a start or end
                var eventObject = {
                    title: $.trim($(this).text()), // use the element's text as the event title
                };
                // store the Event Object in the DOM element so we can get to it later
                $(this).data('eventObject', eventObject);
                // make the event draggable using jQuery UI
                $(this).draggable({
                    zIndex: 999,
                    revert: true, // will cause the event to go back to its
                    revertDuration: 0, //  original position after the drag
                });
            });
        });
    /* Initializing */
    (CalendarApp.prototype.init = function () {
        this.enableDrag();
        /*  Initialize the calendar  */
        var date = new Date();
        var d = date.getDate();
        var m = date.getMonth();
        var y = date.getFullYear();
        var form = '';
        var today = new Date($.now());

        var defaultEvents = [
            {
                title: '완료',
                start: new Date('2021/6/28/08:15:00'),
                end: new Date('2021/6/28/10:30:00'),
                className: 'bg-success',
            },
            {
                title: '실패',
                start: new Date('2021/6/29/18:30:00'),
                end: new Date('2021/6/29/21:00:00'),
                // start: new Date($.now() - 1099000000),
                // end: new Date($.now() - 919000000),
                className: 'bg-danger',
            },
            {
                title: '완료',
                start: new Date('2021/6/30/18:45:00'),
                end: new Date('2021/6/30/19:50:00'),
                className: 'bg-success',
            },
            {
                title: '완료',
                start: new Date('2021/7/1/15:40:00'),
                end: new Date('2021/7/1/17:50:00'),
                className: 'bg-success',
            },
            {
                title: '완료',
                start: new Date('2021/7/2/15:20:00'),
                end: new Date('2021/7/2/16:50:00'),
                className: 'bg-success',
            },
            {
                title: '연기',
                start: new Date('2021/7/3/12:10:00'),
                end: new Date('2021/7/3/14:40:00'),
                className: 'bg-warning',
            },
            {
                title: '헬스장',
                start: new Date('2021/7/7/20:30:00'),
                end: new Date('2021/7/7/22:00:00'),
                className: 'bg-info',
            },
            {
                title: '헬스장',
                start: new Date('2021/7/14/19:30:00'),
                end: new Date('2021/7/14/22:00:00'),
                className: 'bg-info',
            },
            {
                title: '헬스장',
                start: new Date('2021/7/16/10:00:00'),
                end: new Date('2021/7/16/12:00:00'),
                className: 'bg-info',
            },
        ];

        var $this = this;
        $this.$calendarObj = $this.$calendar.fullCalendar({
            slotDuration: '00:15:00',
            /* If we want to split day time each 15minutes */
            minTime: '08:00:00',
            maxTime: '24:00:00',
            defaultView: 'month',
            handleWindowResize: true,

            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay',
            },
            events: defaultEvents,
            editable: true,
            droppable: true, // this allows things to be dropped onto the calendar !!!
            eventLimit: true, // allow "more" link when too many events
            selectable: true,
            drop: function (date) {
                $this.onDrop($(this), date);
            },
            select: function (start, end, allDay) {
                $this.onSelect(start, end, allDay);
            },
            eventClick: function (calEvent, jsEvent, view) {
                $this.onEventClick(calEvent, jsEvent, view);
            },
        });
    }),
        //init CalendarApp
        ($.CalendarApp = new CalendarApp()),
        ($.CalendarApp.Constructor = CalendarApp);
})(window.jQuery),
    //initializing CalendarApp
    $(window).on('load', function () {
        $.CalendarApp.init();
    });
