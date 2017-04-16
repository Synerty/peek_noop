import {Component} from "@angular/core";
import {ComponentLifecycleEventEmitter, VortexService} from "@synerty/vortexjs";
import {noopFilt} from "@peek/peek_plugin_noop/_private";
import {extend} from "@synerty/vortexjs";
import {Ng2BalloonMsgService} from "@synerty/ng2-balloon-msg";

@Component({
    selector: 'plugin-noop-mobile',
    templateUrl: 'noop.component.mweb.html',
    moduleId: module.id
})
export class NoopComponent extends ComponentLifecycleEventEmitter {

    date: string = "No data yet";
    stopped: boolean = false;

    private filt = extend({
        "key": "sendDate"
    }, noopFilt);

    constructor(vortexService: VortexService, private balloonMsg:Ng2BalloonMsgService) {
        super();

        let loader = vortexService.createTupleLoader(this, this.filt);
        loader.observable
            .subscribe(tuples => {
                // Update our value
                this.date = tuples[0];

            });

        this.onDestroyEvent.subscribe(() => {
            this.stopped = true;
        });

        let loadAgain = () => {
            if (this.stopped)
                return;

            // Schedule a reload in 1 second
            setTimeout(() => {
                loadAgain();
                loader.load()
            }, 2000);
        };

        loadAgain();
    }

    sendSuccessMsgClicked() {
        this.balloonMsg.showSuccess("You have clicked the button.", "/");
    }


}