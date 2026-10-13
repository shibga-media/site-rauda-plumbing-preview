"""Generates copy.json. Copy was drafted by Qwen/Kimi, then rewritten after review: every sentence uses only fact-sheet facts
or generic plumbing information. Run: python3 copygen.py"""
import json
SV = {
"drain-cleaning": dict(
 intro="A sink that drains slowly or a tub that takes a long time to empty is usually the first sign of a clog. Soap, hair, grease and everyday debris collect inside drain lines until water can no longer pass freely. {BIZ} is a plumbing company, so drain problems are exactly the kind of call we are set up for.",
 signs=["A sink, tub or shower that drains slowly","Gurgling sounds from a drain","Water backing up in one fixture when another is used","Odors coming from a drain","A clog that keeps coming back"],
 visit="A drain cleaning visit generally starts with finding out where the blockage is. A clog in one sink is a different problem from several drains slowing down at once, which can point to the main line. Once the location is clear, the drain is cleared with the right method for that line, and water flow is checked afterward. If the clog turns out to be part of a bigger problem, such as a damaged or blocked sewer line, that is the time to talk about next steps.",
 more="Kitchen drains tend to collect grease and food particles, while bathroom drains are more likely to hold hair and soap. Toilets can also back up, and a toilet that keeps clogging is worth having checked. Catching a slow drain early is usually simpler than waiting for a full backup."),
"water-heater": dict(
 intro="Hot water is easy to take for granted until it stops. When a water heater fails, leaks or no longer keeps up, it affects showers, laundry and the kitchen all at once. {BIZ} repairs and installs water heaters for homeowners across Middle Tennessee.",
 signs=["No hot water, or water that never gets very warm","Water that runs out quickly","Popping or rumbling noises from the tank","Water pooling around the base of the heater","Rusty or discolored hot water"],
 visit="A water heater visit starts with working out what is wrong: whether the unit can be repaired or has reached the point where replacing it makes more sense. If it can be repaired, the repair is made and the heater is checked. If it needs to be replaced, installation generally means shutting off the water and power or gas, draining and removing the old unit, setting the new one, reconnecting the lines and confirming it heats properly.",
 more="A leak at the base of a tank is one of the signs that should not wait, since a leaking tank can damage the floor around it. If you see water around your heater, shut off the water supply to it if you can do so safely, then call or text to book an appointment."),
"leak-repair": dict(
 intro="A drip under the sink or a damp spot on a wall can look minor, but water that keeps escaping can damage cabinets, flooring and drywall over time. {BIZ} finds and repairs leaks in homes across Murfreesboro and the surrounding area.",
 signs=["Water stains on a ceiling or wall","A damp or musty smell that keeps returning","A dripping pipe or fitting under a sink","The sound of running water when nothing is on","A water bill that climbs without explanation"],
 visit="A leak repair visit generally starts with looking over the area and listening to what you have noticed. Fixtures, fittings, valves and nearby piping are checked to narrow down where the water is coming from. Once the source is found, the repair is made and the line is checked again. Some leaks are easy to see, like a loose connection under a sink. Others are inside walls or under floors and take more checking to locate.",
 more="Supply lines, the lines and hoses that carry water to sinks, toilets and appliances, are a common place for leaks to start. Because they hold water under pressure, even a small leak can release a lot of water over time, so it is better to have it looked at sooner rather than later."),
"sewer-line": dict(
 intro="Your home's sewer line carries waste from every sink, shower and toilet out to the sewer or septic system. When it has a problem, the signs usually show up in more than one place. {BIZ} helps homeowners work out what is happening with their main line and what to do about it.",
 signs=["Several drains backing up at the same time","Gurgling from toilets or floor drains","A sewage smell in the house or yard","Water rising in a tub or shower when another fixture drains","Slow drains throughout the house"],
 visit="Because a sewer line problem is different from a clog in one fixture, a visit generally starts by working out whether the trouble is in a single drain or the main line. From there, the next step depends on what is found: a blockage can often be cleared, while a damaged section of pipe may need repair or replacement. The options are explained so you can decide how to move forward.",
 more="A main line problem is not something that usually clears up on its own. If more than one drain in the house is slow or backing up, it is worth booking an appointment rather than waiting."),
"toilet-faucet-fixtures": dict(
 intro="Running toilets, dripping faucets and worn-out fixtures are some of the most common plumbing calls in any home. They are easy to put off, but a small problem can waste water and get worse. {BIZ} repairs and replaces toilets, faucets and other fixtures.",
 signs=["A toilet that keeps running or refills on its own","A faucet that drips when it is turned off","A toilet that rocks or leaks around the base","Low water pressure at one sink or shower","Handles that are loose, stiff or corroded"],
 visit="A fixture visit generally starts with a look at what is happening, such as where a faucet is dripping from or why a toilet will not stop running. Many problems can be fixed by repairing or replacing the worn part inside the fixture. When a fixture is too worn out to repair sensibly, or you simply want a new one, it can be replaced and the connections checked for leaks.",
 more="You do not need to diagnose the problem before you call. Describe what you are seeing and hearing, and that is enough to book an appointment."),
"repiping": dict(
 intro="Repiping means replacing the supply pipes that bring water through your home. It is a bigger job than a single repair, and it is usually considered when pipes keep failing or are in poor condition. {BIZ} can look at your plumbing and talk through whether repairing or replacing makes sense.",
 signs=["Repeated leaks in different parts of the house","Discolored or rusty water coming from the taps","Low water pressure throughout the house","Visible corrosion on exposed pipes","Pipes that are very old"],
 visit="A repiping conversation generally starts with a look at the existing pipes and the problems you have had. From there you can decide whether a repair is enough or whether replacing a section, or more, is the better step. Replacing pipes involves opening access to the lines, installing the new piping, reconnecting fixtures and checking everything for leaks.",
 more="If you are only having trouble in one spot, a repair may be all you need. If you are seeing problems in several places, it is a good reason to have the whole system looked at."),
"garbage-disposal": dict(
 intro="A garbage disposal that jams, hums, leaks or smells can turn kitchen cleanup into a chore. {BIZ} repairs and replaces garbage disposals for homeowners in Murfreesboro and across Middle Tennessee.",
 signs=["A disposal that hums but does not spin","A disposal that will not turn on","Water leaking from under the sink","Water that drains slowly from the sink","Unpleasant smells that come from the disposal"],
 visit="A disposal visit generally starts with checking whether the unit is jammed, has a leak or has stopped working. A jam can often be cleared and a loose connection can be tightened. If the disposal has failed, it can be replaced and the connections to the sink and drain checked for leaks.",
 more="If the sink is draining slowly, the problem may be the drain line and not the disposal itself, so it is worth describing exactly what you see when you book."),
"emergency-plumbing": dict(
 intro="Some plumbing problems cannot wait for a convenient time: a burst pipe, a major leak, an overflowing toilet or a sewage backup. If you are dealing with one, the first thing to do is to stop the water, then call or text {BIZ}.",
 signs=["A burst or leaking pipe","Water flowing that you cannot stop","A toilet that is overflowing","Sewage backing up into a drain or tub","Water coming through a ceiling"],
 visit="While you are reaching out, shut off the water at the main shutoff valve if you can do so safely. This limits the damage while you wait. When you call or text, describe what is happening and where, so the situation is clear from the start. From there, the plumber works out what is wrong and what needs to be done to fix it.",
 more="If water is near electrical outlets or fixtures, stay away from the area. For an emergency affecting your safety, such as a gas smell, leave the home and call your local emergency number."),
}
CITY = {"murfreesboro":("Rutherford County","our home base"),"columbia":("Maury County",None),"franklin":("Williamson County",None),
 "spring-hill":("Maury and Williamson counties",None),"brentwood":("Williamson County",None),"nashville":("Davidson County",None),
 "smyrna":("Rutherford County",None),"mount-juliet":("Wilson County",None)}
NAMES={"murfreesboro":"Murfreesboro","columbia":"Columbia","franklin":"Franklin","spring-hill":"Spring Hill","brentwood":"Brentwood","nashville":"Nashville","smyrna":"Smyrna","mount-juliet":"Mount Juliet"}
SERV=["drain cleaning","water heater repair and installation","leak repair","sewer line service","toilet, faucet and fixture repair","repiping","garbage disposal repair and replacement","emergency plumbing"]
PREP="It helps to have a few details ready when you call or text: where in the house the problem is, when you first noticed it, and whether it is getting worse. If water is involved, tell us whether you have been able to shut it off. You do not need to know the cause or use plumbing terms. A plain description of what you see, hear or smell is enough to get started, and it makes it easier to work out what needs to be done before anyone arrives at your door."
out={}
for k,v in SV.items():
    out[k]={"paras":[v["intro"],v["visit"],v["more"],"{BIZ} is an owner-operated plumbing company based in Murfreesboro, Tennessee, serving Middle Tennessee since 2020. To book an appointment, call or text. There is no online form."],"bullets":v["signs"]}
    out[k]["paras"].insert(3,PREP)
for k,(cty,base) in CITY.items():
    n=NAMES[k]
    first = (f"{n} is where {{BIZ}} is based. We are an owner-operated plumbing company serving homeowners in {n} and the rest of Middle Tennessee, and plumbing is the only thing we do." if base else
             f"{{BIZ}} is a plumbing company based in Murfreesboro, and {n} in {cty} is one of the places we serve. If you need a plumber in {n}, you can call or text to book an appointment.")
    out[k]={"paras":[first,
      f"Homeowners in {n} call us about the same kinds of problems that come up in any home: drains that will not clear, water heaters that stop working, leaks, running toilets and dripping faucets. Here is what we help with in {n}: "+", ".join(SERV[:-1])+f", and {SERV[-1]}.",
      "Each service has its own page with the signs to watch for and what a visit generally involves. If you are not sure which one fits what you are seeing, that is fine. Describe the problem when you call or text and we will work out the next step.",
      f"If you have a plumbing emergency in {n}, such as a burst pipe or a sewage backup, shut off the water at the main valve if you can do so safely and then call or text right away.",
      PREP,
      f"{{BIZ}} has been serving Middle Tennessee since 2020. To book a plumbing appointment in {n}, call or text. There is no online form, so reaching us by phone is the fastest way to get on the schedule."],
      "bullets":[]}
out["home"]={"paras":[
 "{BIZ} is a plumbing company based in Murfreesboro, Tennessee, serving Middle Tennessee since 2020. We are owner-operated and plumbing is the only trade we do, so every call is a plumbing call.",
 "Homeowners call us for drain cleaning, water heater repair and installation, leak repair, sewer line service, toilet, faucet and fixture repair, repiping, garbage disposal repair and emergency plumbing. Each service has its own page explaining the signs to watch for and what a visit generally involves.",
 "We serve Murfreesboro, Columbia, Smyrna, Mount Juliet, Franklin, Spring Hill, Brentwood and Nashville. Pick your city below to see more about plumbing service where you live.",
 "Booking is simple. Call or text, tell us what is happening, and we will set up an appointment. There is no online form to fill out."],"bullets":[]}
out["about"]={"paras":[
 "{BIZ} is an owner-operated plumbing company based in Murfreesboro, Tennessee. We have been serving Middle Tennessee since 2020.",
 "We do plumbing and only plumbing. That means we are not trying to be everything to everyone: when you call, you are reaching a company whose only business is keeping homes running with working drains, hot water and pipes.",
 "We serve homeowners in Murfreesboro, Columbia, Smyrna, Mount Juliet, Franklin, Spring Hill, Brentwood and Nashville. Our services include drain cleaning, water heater repair and installation, leak repair, sewer line service, toilet, faucet and fixture repair, repiping, garbage disposal repair and emergency plumbing.",
 "To book, call or text. We keep it that simple, with no online form and no runaround. Tell us what is going on and we will set up an appointment."],"bullets":[]}
json.dump(out,open("copy.json","w"),indent=1)
print({k:sum(len(p.split()) for p in v["paras"]) for k,v in out.items()})
